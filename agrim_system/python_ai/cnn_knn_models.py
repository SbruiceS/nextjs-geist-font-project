"""
CNN and KNN models and integration for AgriML system.
Includes CNN for image-based crop disease detection and KNN for classification tasks.
"""

import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

class CNNModel:
    def __init__(self, input_shape=(64, 64, 3), num_classes=5):
        self.model = self.build_model(input_shape, num_classes)

    def build_model(self, input_shape, num_classes):
        model = models.Sequential([
            layers.Conv2D(32, (3,3), activation='relu', input_shape=input_shape),
            layers.MaxPooling2D(2,2),
            layers.Conv2D(64, (3,3), activation='relu'),
            layers.MaxPooling2D(2,2),
            layers.Flatten(),
            layers.Dense(128, activation='relu'),
            layers.Dense(num_classes, activation='softmax')
        ])
        model.compile(optimizer='adam',
                      loss='sparse_categorical_crossentropy',
                      metrics=['accuracy'])
        return model

    def train(self, x_train, y_train, epochs=10, batch_size=32):
        self.model.fit(x_train, y_train, epochs=epochs, batch_size=batch_size)

    def predict(self, x):
        preds = self.model.predict(x)
        return np.argmax(preds, axis=1)

class KNNModel:
    def __init__(self, n_neighbors=3):
        self.scaler = StandardScaler()
        self.knn = KNeighborsClassifier(n_neighbors=n_neighbors)

    def train(self, X_train, y_train):
        X_scaled = self.scaler.fit_transform(X_train)
        self.knn.fit(X_scaled, y_train)

    def predict(self, X_test):
        X_scaled = self.scaler.transform(X_test)
        return self.knn.predict(X_scaled)

def integrate_models(cnn_model, knn_model, cnn_data, knn_data):
    """
    Example integration function combining CNN and KNN predictions.
    cnn_data: image data for CNN
    knn_data: feature data for KNN
    Returns combined prediction.
    """
    cnn_preds = cnn_model.predict(cnn_data)
    knn_preds = knn_model.predict(knn_data)

    # Simple voting or weighted average can be implemented here
    combined_preds = []
    for c_pred, k_pred in zip(cnn_preds, knn_preds):
        if c_pred == k_pred:
            combined_preds.append(c_pred)
        else:
            # If disagreement, choose CNN prediction (example)
            combined_preds.append(c_pred)
    return combined_preds
