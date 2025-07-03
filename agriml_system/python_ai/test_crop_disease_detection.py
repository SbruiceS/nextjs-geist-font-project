import grpc
import agriml_pb2
import agriml_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50053')
    stub = agriml_pb2_grpc.CropDiseaseDetectionServiceStub(channel)

    # Dummy image data for testing
    image_data = b'\x00' * (64 * 64 * 3)

    request = agriml_pb2.CropImage(image_data=image_data)
    response = stub.DetectDisease(request)

    print(f"Disease: {response.disease_name}, Confidence: {response.confidence}")

if __name__ == '__main__':
    run()
