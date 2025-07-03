//! Rust module for soil moisture data collection and streaming using gRPC.

use tonic::{transport::Server, Request, Response, Status};
use agriml::soil_moisture_service_server::{SoilMoistureService, SoilMoistureServiceServer};
use agriml::{SoilMoistureData, StreamResponse};
use tokio::sync::mpsc;
use tokio_stream::wrappers::ReceiverStream;

pub mod agriml {
    tonic::include_proto!("agriml");
}

#[derive(Debug, Default)]
pub struct SoilMoistureServiceImpl {}

#[tonic::async_trait]
impl SoilMoistureService for SoilMoistureServiceImpl {
    async fn stream_soil_moisture_data(
        &self,
        request: Request<SoilMoistureData>,
    ) -> Result<Response<StreamResponse>, Status> {
        let data = request.into_inner();
        println!(
            "Received soil moisture data from device {}: moisture_level={}, temperature={}, pH={}, timestamp={}",
            data.device_id, data.moisture_level, data.temperature, data.ph_level, data.timestamp
        );

        // AI-based anomaly detection example
        if data.moisture_level < 10.0 {
            println!("Warning: Low soil moisture detected for device {}", data.device_id);
            // Additional AI logic can be added here
        }

        // Example: Publish data to Kafka topic "soil_moisture"
        let kafka_client = KafkaClient::new("localhost:9092", "rust_edge_group");
        let payload = format!(
            "{{\"device_id\":\"{}\",\"moisture_level\":{},\"temperature\":{},\"ph_level\":{},\"timestamp\":{}}}",
            data.device_id, data.moisture_level, data.temperature, data.ph_level, data.timestamp
        );
        tokio::spawn(async move {
            kafka_client.send_message("soil_moisture", &payload).await;
        });

        let reply = StreamResponse {
            status: "Data received and forwarded".into(),
        };
        Ok(Response::new(reply))
    }
}

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let addr = "[::1]:50051".parse()?;
    let soil_moisture_service = SoilMoistureServiceImpl::default();

    println!("SoilMoistureServiceServer listening on {}", addr);

    Server::builder()
        .add_service(SoilMoistureServiceServer::new(soil_moisture_service))
        .serve(addr)
        .await?;

    Ok(())
}
