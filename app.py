import os
import time
from datetime import datetime
from functools import wraps
from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify, send_from_directory
from werkzeug.utils import secure_filename

from config import SECRET_KEY, UPLOAD_FOLDER, DATASET_SAMPLES_DIR, ALLOWED_EXTENSIONS
from database import (
    init_db, register_user, authenticate_user, get_user_by_id, 
    save_diagnosis, get_user_diagnoses, get_diagnosis_by_id, get_analytics_summary
)
from model_loader import predict_crop_disease, get_reference_sample_images, compute_image_similarity
from disease_data import ORDERED_CLASSES, DISEASE_PROFILES, get_disease_profile

# Initialize Flask app
app = Flask(__name__)
app.secret_key = SECRET_KEY
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB

# Initialize database schema on startup
init_db()

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash("Please sign in to access this page.", "warning")
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

# Context processor for global template variables
@app.context_processor
def inject_user():
    return {
        'logged_in': 'user_id' in session,
        'current_user_id': session.get('user_id'),
        'current_username': session.get('username'),
        'current_full_name': session.get('full_name')
    }

# ----------------- AUTHENTICATION ROUTES ----------------- #

@app.route('/register', methods=['GET', 'POST'])
def register():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        full_name = request.form.get('full_name', '').strip()
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')
        confirm_password = request.form.get('confirm_password', '')
        farm_location = request.form.get('farm_location', 'Agricultural Land').strip()
        crop_interests = request.form.get('crop_interests', 'Tomato, Potato, Corn, Apple').strip()

        if not username or not full_name or not email or not password:
            flash("Please fill in all required fields.", "danger")
            return render_template('register.html')

        if password != confirm_password:
            flash("Passwords do not match.", "danger")
            return render_template('register.html')

        if len(password) < 6:
            flash("Password must be at least 6 characters long.", "danger")
            return render_template('register.html')

        user_id, error = register_user(username, full_name, email, password, farm_location, crop_interests)
        if error:
            flash(f"Registration failed: {error}", "danger")
            return render_template('register.html')

        flash(f"Account successfully created! Your Unique Farmer ID is: {user_id}. Please log in.", "success")
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        identifier = request.form.get('identifier', '').strip()
        password = request.form.get('password', '')

        if not identifier or not password:
            flash("Please provide your Username / User ID and password.", "danger")
            return render_template('login.html')

        user = authenticate_user(identifier, password)
        if user:
            session['user_id'] = user['user_id']
            session['username'] = user['username']
            session['full_name'] = user['full_name']
            flash(f"Welcome back, {user['full_name']}! (User ID: {user['user_id']})", "success")
            
            next_url = request.args.get('next')
            return redirect(next_url if next_url else url_for('dashboard'))
        else:
            flash("Invalid credentials. Please verify your User ID/Username and password.", "danger")

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash("You have been signed out safely.", "info")
    return redirect(url_for('login'))

@app.route('/profile')
@login_required
def profile():
    user = get_user_by_id(session['user_id'])
    stats = get_analytics_summary(session['user_id'])
    recent_diagnoses = get_user_diagnoses(session['user_id'], limit=5)
    return render_template('profile.html', user=user, stats=stats, recent_diagnoses=recent_diagnoses)

# ----------------- MAIN APP & DIAGNOSIS ----------------- #

@app.route('/')
def home():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    if request.method == 'POST':
        if 'leaf_image' not in request.files:
            flash("No file part selected.", "danger")
            return redirect(request.url)

        file = request.files['leaf_image']
        if file.filename == '':
            flash("No file was selected for upload.", "warning")
            return redirect(request.url)

        if not allowed_file(file.filename):
            flash("Invalid file format. Please upload JPG, PNG, or WEBP images.", "danger")
            return redirect(request.url)

        # Secure filename with timestamp
        ext = file.filename.rsplit('.', 1)[1].lower()
        unique_name = f"{session['user_id']}_{int(time.time())}_{secure_filename(file.filename)}"
        save_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_name)
        file.save(save_path)

        try:
            # Run MobileNetV2 prediction & comparison
            result = predict_crop_disease(save_path)

            # Save diagnosis to database
            diag_id = save_diagnosis(
                user_id=session['user_id'],
                image_filename=unique_name,
                predicted_class=result['predicted_class'],
                crop_name=result['crop'],
                condition_name=result['condition'],
                confidence=result['confidence'],
                severity=result['severity'],
                similarity_score=result['similarity_score'],
                reference_image=result['reference_sample'] or '',
                notes=request.form.get('notes', '')
            )

            return redirect(url_for('view_diagnosis', diag_id=diag_id))
        except Exception as e:
            flash(f"Error during image analysis: {str(e)}", "danger")
            return redirect(request.url)

    # GET request - show dashboard upload view
    stats = get_analytics_summary(session['user_id'])
    recent_diagnoses = get_user_diagnoses(session['user_id'], limit=6)
    return render_template('index.html', stats=stats, recent_diagnoses=recent_diagnoses)

@app.route('/diagnosis/<int:diag_id>')
@login_required
def view_diagnosis(diag_id):
    diag = get_diagnosis_by_id(diag_id)
    if not diag:
        flash("Diagnosis record not found.", "warning")
        return redirect(url_for('dashboard'))

    # Load profile data
    profile = get_disease_profile(diag['predicted_class'])
    
    # Retrieve reference samples
    ref_sample, healthy_sample = get_reference_sample_images(diag['predicted_class'])

    # Re-calculate detailed comparison metrics
    upload_path = os.path.join(app.config['UPLOAD_FOLDER'], diag['image_filename'])
    ref_path = os.path.join(app.static_folder, ref_sample) if ref_sample else None

    similarity_score = diag['similarity_score']
    comparison_metrics = {"color_match": 85.0, "texture_match": 80.0}
    if ref_path and os.path.exists(ref_path) and os.path.exists(upload_path):
        similarity_score, comparison_metrics = compute_image_similarity(upload_path, ref_path)

    return render_template(
        'result.html',
        diag=diag,
        profile=profile,
        ref_sample=ref_sample,
        healthy_sample=healthy_sample,
        similarity_score=similarity_score,
        comparison_metrics=comparison_metrics
    )

# ----------------- DATASET COMPARISON & EXPLORER ----------------- #

@app.route('/compare', methods=['GET', 'POST'])
@login_required
def compare():
    selected_class = request.args.get('class_name', 'Tomato___Early_blight')
    if selected_class not in ORDERED_CLASSES:
        selected_class = 'Tomato___Early_blight'

    profile = get_disease_profile(selected_class)
    ref_sample, healthy_sample = get_reference_sample_images(selected_class)
    
    uploaded_image_url = None
    similarity_data = None

    if request.method == 'POST' and 'custom_leaf' in request.files:
        file = request.files['custom_leaf']
        if file and file.filename != '' and allowed_file(file.filename):
            unique_name = f"compare_{int(time.time())}_{secure_filename(file.filename)}"
            upload_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_name)
            file.save(upload_path)
            uploaded_image_url = url_for('static', filename=f"uploads/{unique_name}")

            # Compute similarity with chosen class reference
            if ref_sample:
                ref_path = os.path.join(app.static_folder, ref_sample)
                sim_score, metrics = compute_image_similarity(upload_path, ref_path)
                similarity_data = {
                    "score": sim_score,
                    "metrics": metrics
                }

    return render_template(
        'compare.html',
        classes=ORDERED_CLASSES,
        selected_class=selected_class,
        profile=profile,
        ref_sample=ref_sample,
        healthy_sample=healthy_sample,
        uploaded_image_url=uploaded_image_url,
        similarity_data=similarity_data
    )

@app.route('/library')
@login_required
def library():
    crop_filter = request.args.get('crop', 'all')
    status_filter = request.args.get('status', 'all')
    search_query = request.args.get('q', '').strip().lower()

    # Collect unique crops
    all_crops = sorted(list(set(c.split('___')[0].replace('_', ' ') for c in ORDERED_CLASSES)))

    disease_list = []
    for cls in ORDERED_CLASSES:
        prof = get_disease_profile(cls)
        crop_clean = prof['crop']
        
        # Filtering
        if crop_filter != 'all' and crop_filter.lower() not in crop_clean.lower():
            continue
        if status_filter != 'all' and status_filter.lower() != prof['status'].lower():
            continue
        if search_query:
            combined_txt = f"{prof['crop']} {prof['condition']} {prof['scientific_name']}".lower()
            if search_query not in combined_txt:
                continue

        ref_sample, _ = get_reference_sample_images(cls)
        disease_list.append({
            "class_name": cls,
            "profile": prof,
            "sample_image": ref_sample
        })

    return render_template(
        'library.html',
        diseases=disease_list,
        crops=all_crops,
        current_crop=crop_filter,
        current_status=status_filter,
        search_query=search_query
    )

@app.route('/history')
@login_required
def history():
    diagnoses = get_user_diagnoses(session['user_id'], limit=100)
    return render_template('history.html', diagnoses=diagnoses)

@app.route('/analytics')
@login_required
def analytics():
    user_stats = get_analytics_summary(session['user_id'])
    global_stats = get_analytics_summary()
    return render_template('analytics.html', user_stats=user_stats, global_stats=global_stats)

# ----------------- API ENDPOINTS ----------------- #

@app.route('/api/predict', methods=['POST'])
def api_predict():
    if 'leaf_image' not in request.files:
        return jsonify({"success": False, "error": "No leaf_image provided"}), 400
    
    file = request.files['leaf_image']
    if not allowed_file(file.filename):
        return jsonify({"success": False, "error": "Invalid file type"}), 400

    filename = f"api_{int(time.time())}_{secure_filename(file.filename)}"
    path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(path)

    try:
        res = predict_crop_disease(path)
        return jsonify({"success": True, "data": res})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/api/class/<class_name>')
def api_class_info(class_name):
    if class_name in ORDERED_CLASSES:
        return jsonify({"success": True, "profile": get_disease_profile(class_name)})
    return jsonify({"success": False, "error": "Class not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
