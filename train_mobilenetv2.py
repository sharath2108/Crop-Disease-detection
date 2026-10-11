"""
Crop Disease Detection - MobileNetV2 Model Training Script
Trains a transfer learning Convolutional Neural Network (CNN) 
based on the MobileNetV2 architecture on the PlantVillage dataset.
"""

import os
import argparse
import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Dropout, BatchNormalization
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping, ReduceLROnPlateau
from tensorflow.keras.preprocessing.image import ImageDataGenerator

IMG_SIZE = (224, 224)
BATCH_SIZE = 32
DEFAULT_EPOCHS = 15
DEFAULT_LR = 0.0001

def build_mobilenetv2_model(num_classes, fine_tune_layers=20):
    """
    Constructs the MobileNetV2 transfer learning model:
    - Base: MobileNetV2 pretrained on ImageNet (weights='imagenet')
    - Top: GlobalAveragePooling2D -> Dense(256) -> BatchNorm -> Dropout(0.4) -> Softmax(num_classes)
    """
    base_model = MobileNetV2(
        weights='imagenet',
        include_top=False,
        input_shape=IMG_SIZE + (3,)
    )

    # Freeze base model layers initially
    base_model.trainable = False

    # Optional fine-tuning of the last n layers
    if fine_tune_layers > 0:
        for layer in base_model.layers[-fine_tune_layers:]:
            layer.trainable = True

    x = base_model.output
    x = GlobalAveragePooling2D(name='global_avg_pool')(x)
    x = Dense(256, activation='relu', name='dense_features')(x)
    x = BatchNormalization(name='batch_norm')(x)
    x = Dropout(0.4, name='dropout_regularization')(x)
    predictions = Dense(num_classes, activation='softmax', name='class_predictions')(x)

    model = Model(inputs=base_model.input, outputs=predictions, name='CropDisease_MobileNetV2')
    return model

def train(dataset_dir, output_model_path='models/crop_disease_model.h5', epochs=DEFAULT_EPOCHS, batch_size=BATCH_SIZE):
    if not os.path.exists(dataset_dir):
        raise FileNotFoundError(f"Dataset directory not found: {dataset_dir}")

    print("Configuring ImageDataGenerator with real-time data augmentation...")
    train_datagen = ImageDataGenerator(
        rescale=1.0 / 255.0,
        rotation_range=25,
        width_shift_range=0.15,
        height_shift_range=0.15,
        shear_range=0.15,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest',
        validation_split=0.2
    )

    print(f"Loading training images from {dataset_dir}...")
    train_gen = train_datagen.flow_from_directory(
        dataset_dir,
        target_size=IMG_SIZE,
        batch_size=batch_size,
        class_mode='categorical',
        subset='training',
        shuffle=True
    )

    print(f"Loading validation images from {dataset_dir}...")
    val_gen = train_datagen.flow_from_directory(
        dataset_dir,
        target_size=IMG_SIZE,
        batch_size=batch_size,
        class_mode='categorical',
        subset='validation',
        shuffle=False
    )

    num_classes = len(train_gen.class_indices)
    print(f"\nDiscovered {num_classes} classes: {list(train_gen.class_indices.keys())}")

    model = build_mobilenetv2_model(num_classes=num_classes)
    model.compile(
        optimizer=Adam(learning_rate=DEFAULT_LR),
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )
    model.summary()

    # Callbacks
    os.makedirs(os.path.dirname(output_model_path) or '.', exist_ok=True)
    callbacks = [
        ModelCheckpoint(output_model_path, monitor='val_accuracy', save_best_only=True, verbose=1),
        EarlyStopping(monitor='val_loss', patience=4, restore_best_weights=True, verbose=1),
        ReduceLROnPlateau(monitor='val_loss', factor=0.5, patience=2, verbose=1, min_lr=1e-6)
    ]

    print("\nStarting MobileNetV2 Training...")
    history = model.fit(
        train_gen,
        steps_per_epoch=max(1, train_gen.samples // batch_size),
        validation_data=val_gen,
        validation_steps=max(1, val_gen.samples // batch_size),
        epochs=epochs,
        callbacks=callbacks
    )

    print(f"\nModel training finished! Best model saved to: {output_model_path}")
    return history

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Train MobileNetV2 CNN for Crop Disease Detection")
    parser.add_argument('--dataset', type=str, default='C:/Users/Sharath/OneDrive/Desktop/Folder/PlantVillage/train',
                        help='Path to PlantVillage training directory')
    parser.add_argument('--output', type=str, default='models/crop_disease_model.h5',
                        help='Destination path for trained model file')
    parser.add_argument('--epochs', type=int, default=DEFAULT_EPOCHS, help='Number of training epochs')
    parser.add_argument('--batch_size', type=int, default=BATCH_SIZE, help='Batch size')
    args = parser.parse_args()

    train(args.dataset, args.output, args.epochs, args.batch_size)
