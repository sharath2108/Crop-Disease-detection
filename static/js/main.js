// AgriVision Main JavaScript

document.addEventListener('DOMContentLoaded', function () {
    const dropZone = document.getElementById('dropZone');
    const fileInput = document.getElementById('fileInput');
    const uploadPrompt = document.getElementById('uploadPrompt');
    const previewContainer = document.getElementById('previewContainer');
    const imagePreview = document.getElementById('imagePreview');
    const previewFilename = document.getElementById('previewFilename');
    const removeImageBtn = document.getElementById('removeImageBtn');
    const uploadForm = document.getElementById('uploadForm');
    const submitBtn = document.getElementById('submitBtn');

    if (dropZone && fileInput) {
        // Trigger file input click when dropzone is clicked
        dropZone.addEventListener('click', function (e) {
            if (e.target !== removeImageBtn && !removeImageBtn.contains(e.target)) {
                fileInput.click();
            }
        });

        // Drag and drop event listeners
        ['dragenter', 'dragover'].forEach(eventName => {
            dropZone.addEventListener(eventName, function (e) {
                e.preventDefault();
                e.stopPropagation();
                dropZone.classList.add('border-brand-500', 'bg-brand-50/50');
            }, false);
        });

        ['dragleave', 'drop'].forEach(eventName => {
            dropZone.addEventListener(eventName, function (e) {
                e.preventDefault();
                e.stopPropagation();
                dropZone.classList.remove('border-brand-500', 'bg-brand-50/50');
            }, false);
        });

        // Handle drop
        dropZone.addEventListener('drop', function (e) {
            const dt = e.dataTransfer;
            const files = dt.files;
            if (files && files.length > 0) {
                fileInput.files = files;
                handleFileSelection(files[0]);
            }
        });

        // Handle file input change
        fileInput.addEventListener('change', function () {
            if (fileInput.files && fileInput.files.length > 0) {
                handleFileSelection(fileInput.files[0]);
            }
        });

        // Remove image selection
        if (removeImageBtn) {
            removeImageBtn.addEventListener('click', function (e) {
                e.stopPropagation();
                fileInput.value = '';
                previewContainer.classList.add('hidden');
                previewContainer.classList.remove('flex');
                uploadPrompt.classList.remove('hidden');
            });
        }
    }

    function handleFileSelection(file) {
        if (!file.type.startsWith('image/')) {
            alert('Please select a valid image file (JPG, PNG, WEBP).');
            return;
        }

        const reader = new FileReader();
        reader.onload = function (e) {
            imagePreview.src = e.target.result;
            previewFilename.textContent = file.name + ' (' + (file.size / 1024).toFixed(1) + ' KB)';
            uploadPrompt.classList.add('hidden');
            previewContainer.classList.remove('hidden');
            previewContainer.classList.add('flex');
        };
        reader.readAsDataURL(file);
    }

    // Submit button loading animation
    if (uploadForm && submitBtn) {
        uploadForm.addEventListener('submit', function () {
            submitBtn.disabled = true;
            submitBtn.innerHTML = `
                <i class="fa-solid fa-spinner fa-spin text-lg mr-2"></i>
                <span>Analyzing Leaf with MobileNetV2 & Comparing Stored Dataset...</span>
            `;
            submitBtn.classList.add('opacity-80', 'cursor-not-allowed');
        });
    }
});
