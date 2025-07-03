// C++ module for weather data processing and decision making using gRPC

#include <iostream>
#include <memory>
#include <string>
#include <grpcpp/grpcpp.h>
#include "agriml.grpc.pb.h"

using grpc::Server;
using grpc::ServerBuilder;
using grpc::ServerContext;
using grpc::Status;
using agriml::WeatherData;
using agriml::WeatherDecision;
using agriml::WeatherProcessingService;

class WeatherProcessingServiceImpl final : public WeatherProcessingService::Service {
    Status ProcessWeatherData(ServerContext* context, const WeatherData* request,
                              WeatherDecision* reply) override {
        std::cout << "Received weather data: Temperature=" << request->temperature()
                  << ", Humidity=" << request->humidity()
                  << ", Rainfall=" << request->rainfall()
                  << ", Wind Speed=" << request->wind_speed()
                  << ", Timestamp=" << request->timestamp() << std::endl;

        // Enhanced decision logic example
        std::string decision;
        std::string recommendation;
        if (request->rainfall() > 10.0) {
            decision = "Delay irrigation due to heavy rainfall";
            recommendation = "Suspend irrigation for 24 hours and monitor soil moisture.";
        } else if (request->temperature() > 35.0) {
            decision = "Increase irrigation due to high temperature";
            recommendation = "Increase irrigation frequency and volume by 20%.";
        } else if (request->wind_speed() > 20.0) {
            decision = "Adjust irrigation due to high wind speed";
            recommendation = "Use drip irrigation to reduce evaporation losses.";
        } else if (request->humidity() < 30.0) {
            decision = "Increase irrigation due to low humidity";
            recommendation = "Increase irrigation frequency to prevent crop stress.";
        } else {
            decision = "Normal irrigation schedule";
            recommendation = "Maintain current irrigation practices.";
        }

        // Kafka publish example
        std::string brokers = "localhost:9092";
        std::string topic = "weather_data";
        std::string payload = "{ \"temperature\": " + std::to_string(request->temperature()) +
                              ", \"humidity\": " + std::to_string(request->humidity()) +
                              ", \"rainfall\": " + std::to_string(request->rainfall()) +
                              ", \"wind_speed\": " + std::to_string(request->wind_speed()) +
                              ", \"timestamp\": " + std::to_string(request->timestamp()) + " }";

        // Initialize Kafka client and send message
        static KafkaClient kafka_client("localhost:9092", "cpp_weather_group");
        kafka_client.send_message(topic, payload);

        reply->set_decision(decision);
        reply->set_timestamp(request->timestamp());
        reply->set_recommendation(recommendation);

        return Status::OK;
    }
};

void RunServer() {
    std::string server_address("0.0.0.0:50052");
    WeatherProcessingServiceImpl service;

    ServerBuilder builder;
    builder.AddListeningPort(server_address, grpc::InsecureServerCredentials());
    builder.RegisterService(&service);

    std::unique_ptr<Server> server(builder.BuildAndStart());
    std::cout << "WeatherProcessingService server listening on " << server_address << std::endl;

    server->Wait();
}

int main(int argc, char** argv) {
    RunServer();
    return 0;
}
