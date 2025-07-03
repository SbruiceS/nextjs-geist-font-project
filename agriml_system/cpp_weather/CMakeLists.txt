cmake_minimum_required(VERSION 3.14)
project(cpp_weather)

set(CMAKE_CXX_STANDARD 17)

find_package(Protobuf REQUIRED)
find_package(gRPC REQUIRED)

include_directories(${Protobuf_INCLUDE_DIRS})

add_executable(weather_processing weather_processing.cpp)

target_link_libraries(weather_processing
    grpc++
    protobuf::libprotobuf
)
