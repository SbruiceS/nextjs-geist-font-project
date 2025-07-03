use tonic::transport::Channel;
use agriml::soil_moisture_service_client::SoilMoistureServiceClient;
use agriml::SoilMoistureData;

pub mod agriml {
    tonic::include_proto!("agriml");
}

#[tokio::test]
async fn test_stream_soil_moisture_data() {
    let mut client = SoilMoistureServiceClient::connect("http://[::1]:50051")
        .await
        .expect("Failed to connect to server");

    let request = tonic::Request::new(SoilMoistureData {
        device_id: "device123".to_string(),
        moisture_level: 42.5,
        timestamp: 1625247600,
    });

    let response = client
        .stream_soil_moisture_data(request)
        .await
        .expect("Failed to send soil moisture data");

    assert_eq!(response.get_ref().status, "Data received");
}
