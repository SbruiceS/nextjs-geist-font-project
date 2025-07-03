"""
Advanced crop analysis models for AgriML system.
Includes:
- Crop type identification (image-based)
- Crop stage detection
- Intercrop detection and ratio analysis
- Weed vs crop segmentation (U-Net)
- Field boundary detection (satellite + ML)
"""

import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np

def build_crop_type_model(input_shape=(224, 224, 3), num_classes=10):
    base_model = tf.keras.applications.EfficientNetB0(input_shape=input_shape,
                                                      include_top=False,
                                                      weights='imagenet')
    base_model.trainable = False
    model = models.Sequential([
        base_model,
        layers.GlobalAveragePooling2D(),
        layers.Dense(128, activation='relu'),
        layers.Dropout(0.3),
        layers.Dense(num_classes, activation='softmax')
    ])
    return model

def build_crop_stage_model(input_shape=(224, 224, 3), num_classes=4):
    model = models.Sequential([
        layers.Conv2D(32, (3,3), activation='relu', input_shape=input_shape),
        layers.MaxPooling2D(2,2),
        layers.Conv2D(64, (3,3), activation='relu'),
        layers.MaxPooling2D(2,2),
        layers.Flatten(),
        layers.Dense(128, activation='relu'),
        layers.Dense(num_classes, activation='softmax')
    ])
    return model

def build_intercrop_ratio_model(input_shape=(224, 224, 3)):
    # Simple CNN to classify intercrop presence and estimate ratio
    model = models.Sequential([
        layers.Conv2D(32, (3,3), activation='relu', input_shape=input_shape),
        layers.MaxPooling2D(2,2),
        layers.Conv2D(64, (3,3), activation='relu'),
        layers.MaxPooling2D(2,2),
        layers.Flatten(),
        layers.Dense(64, activation='relu'),
        layers.Dense(1, activation='sigmoid')  # Output ratio between 0 and 1
    ])
    return model

def build_unet_segmentation_model(input_shape=(256, 256, 3), num_classes=2):
    inputs = layers.Input(shape=input_shape)

    # Encoder
    c1 = layers.Conv2D(64, (3,3), activation='relu', padding='same')(inputs)
    c1 = layers.Conv2D(64, (3,3), activation='relu', padding='same')(c1)
    p1 = layers.MaxPooling2D((2,2))(c1)

    c2 = layers.Conv2D(128, (3,3), activation='relu', padding='same')(p1)
    c2 = layers.Conv2D(128, (3,3), activation='relu', padding='same')(c2)
    p2 = layers.MaxPooling2D((2,2))(c2)

    c3 = layers.Conv2D(256, (3,3), activation='relu', padding='same')(p2)
    c3 = layers.Conv2D(256, (3,3), activation='relu', padding='same')(c3)
    p3 = layers.MaxPooling2D((2,2))(c3)

    # Bottleneck
    b = layers.Conv2D(512, (3,3), activation='relu', padding='same')(p3)
    b = layers.Conv2D(512, (3,3), activation='relu', padding='same')(b)

    # Decoder
    u3 = layers.UpSampling2D((2,2))(b)
    u3 = layers.concatenate([u3, c3])
    c4 = layers.Conv2D(256, (3,3), activation='relu', padding='same')(u3)
    c4 = layers.Conv2D(256, (3,3), activation='relu', padding='same')(c4)

    u2 = layers.UpSampling2D((2,2))(c4)
    u2 = layers.concatenate([u2, c2])
    c5 = layers.Conv2D(128, (3,3), activation='relu', padding='same')(u2)
    c5 = layers.Conv2D(128, (3,3), activation='relu', padding='same')(c5)

    u1 = layers.UpSampling2D((2,2))(c5)
    u1 = layers.concatenate([u1, c1])
    c6 = layers.Conv2D(64, (3,3), activation='relu', padding='same')(u1)
    c6 = layers.Conv2D(64, (3,3), activation='relu', padding='same')(c6)

    outputs = layers.Conv2D(num_classes, (1,1), activation='softmax')(c6)

    model = models.Model(inputs=[inputs], outputs=[outputs])
    return model

def build_field_boundary_detection_model(input_shape=(256, 256, 3)):
    # Simple CNN for satellite image classification of field boundaries
    model = models.Sequential([
        layers.Conv2D(32, (3,3), activation='relu', input_shape=input_shape),
        layers.MaxPooling2D(2,2),
        layers.Conv2D(64, (3,3), activation='relu'),
        layers.MaxPooling2D(2,2),
        layers.Flatten(),
        layers.Dense(128, activation='relu'),
        layers.Dense(1, activation='sigmoid')  # Binary classification: boundary or not
    ])
    return model
