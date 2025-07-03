// Simple test for WeatherProcessingService

#include <iostream>
#include <grpcpp/grpcpp.h>
#include "agriml.grpc.pb.h"

using grpc::Channel;
using grpc::ClientContext;
using grpc::Status;
using agriml::WeatherData;
using agriml::WeatherDecision;
using agriml::WeatherProcessingService;

class WeatherProcessingClient {
public:
    WeatherProcessingClient(std::shared_ptr<Channel> channel)
        : stub_(WeatherProcessingService::NewStub(channel)) {}

    std::string ProcessWeatherData(double temperature, double humidity, double rainfall, int64_t timestamp) {
        WeatherData request;
        request.set_temperature(temperature);
        request.set_humidity(humidity);
        request.set_rainfall(rainfall);
        request.set_timestamp(timestamp);

        WeatherDecision reply;
        ClientContext context;

        Status status = stub_->ProcessWeatherData(&context, request, &reply);

        if (status.ok()) {
            return reply.decision();
        } else {
            std::cerr << "RPC failed" << std::endl;
            return "RPC failed";
        }
    }

private:
    std::unique_ptr<WeatherProcessingService::Stub> stub_;
};

int main() {
    WeatherProcessingClient client(grpc::CreateChannel("localhost:50052", grpc::InsecureChannelCredentials()));

    std::string decision = client.ProcessWeatherData(36.5, 50.0, 5.0, 1625247600);
    std::cout << "Decision: " << decision << std::endl;

    return 0;
}
