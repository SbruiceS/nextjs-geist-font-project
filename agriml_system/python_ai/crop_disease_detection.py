import grpc
from concurrent import futures
import time
import agriml_pb2
import agriml_pb2_grpc
import tensorflow as tf
import numpy as np
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image
import io
from cnn_knn_models import CNNModel, KNNModel

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class CropDiseaseDetectionServicer(agriml_pb2_grpc.CropDiseaseDetectionServiceServicer):
    def __init__(self):
        # Load CNN and KNN models
        self.cnn_model = CNNModel()
        self.knn_model = KNNModel()

        # Dummy training or loading weights can be added here

    def preprocess_image(self, image_bytes):
        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
        image = image.resize((64, 64))
        image = img_to_array(image)
        image = np.expand_dims(image, axis=0)
        return image

    def DetectDisease(self, request, context):
        image_bytes = request.image_data
        crop_type = request.crop_type

        input_data = self.preprocess_image(image_bytes)

        # CNN prediction
        cnn_pred = self.cnn_model.predict(input_data)[0]

        # Dummy KNN feature vector (replace with real features)
        knn_features = np.array([[0.5, 0.3, 0.2]])
        knn_pred = self.knn_model.predict(knn_features)[0]

        # Integration logic
        if cnn_pred == knn_pred:
            final_pred = cnn_pred
        else:
            final_pred = cnn_pred  # Prefer CNN prediction

        disease_names = ['DiseaseA', 'DiseaseB', 'DiseaseC', 'DiseaseD', 'DiseaseE']
        disease_name = disease_names[final_pred]

        confidence = 0.9  # Dummy confidence

        treatments = {
            'DiseaseA': 'Use fungicide A',
            'DiseaseB': 'Apply pesticide B',
            'DiseaseC': 'Increase irrigation',
            'DiseaseD': 'Use organic treatment D',
            'DiseaseE': 'Consult expert'
        }
        treatment = treatments.get(disease_name, 'No treatment available')

        return agriml_pb2.DiseasePrediction(disease_name=disease_name, confidence=confidence, treatment=treatment)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    agriml_pb2_grpc.add_CropDiseaseDetectionServiceServicer_to_server(CropDiseaseDetectionServicer(), server)
    server.add_insecure_port('[::]:50053')
    server.start()
    print("CropDiseaseDetectionService server started on port 50053.")
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
