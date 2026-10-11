import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Security & Sessions
SECRET_KEY = os.environ.get('SECRET_KEY', 'crop_vision_mobilenetv2_secret_key_2026_xyz')

# Paths
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'static', 'uploads')
MODEL_PATH = os.path.join(BASE_DIR, 'models', 'crop_disease_model.h5')
DATASET_SAMPLES_DIR = os.path.join(BASE_DIR, 'static', 'dataset_samples')
DB_PATH = os.path.join(BASE_DIR, 'crop_disease.db')

# Ensure directories exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(DATASET_SAMPLES_DIR, exist_ok=True)
os.makedirs(os.path.join(BASE_DIR, 'models'), exist_ok=True)

# Image upload parameters
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'webp', 'jfif'}
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB max upload
IMG_SIZE = (224, 224)

# Model inference settings
CONFIDENCE_THRESHOLD_LOW = 40.0
CONFIDENCE_THRESHOLD_HIGH = 75.0
