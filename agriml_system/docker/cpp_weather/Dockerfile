# C++ Weather Module Dockerfile
FROM ubuntu:20.04

RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    libssl-dev \
    librdkafka-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY ../../cpp_weather /app

RUN mkdir build && cd build && cmake .. && make

EXPOSE 50052

USER nobody

CMD ["./build/weather_processing"]
