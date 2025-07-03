# AgriML System

This project is a high-performance AgriML system designed for real-time agricultural analytics, weather-based decisions, and AI automation across edge devices and cloud. It integrates Rust, C++, and Python (Keras) components with gRPC interfaces for cross-language communication.

## Folder Structure

- `proto/` - Protobuf definitions for gRPC interfaces shared by all components.
- `rust_edge/` - Rust module for soil moisture data collection and streaming.
- `cpp_weather/` - C++ module for weather data processing and decision making.
- `python_ai/` - Python module with Keras crop disease detection model and gRPC server.

## Components

### Rust Edge Module

- Implements a gRPC server to stream soil moisture data.
- Uses `tonic` and `tokio` for async gRPC server.
- Includes integration test with mock data.

### C++ Weather Module

- Implements a gRPC server to process weather data and make irrigation decisions.
- Uses gRPC C++ library.
- Includes a test client with mock weather data.
- Build with CMake.

### Python AI Module

- Implements a gRPC server for crop disease detection using a Keras model.
- Dummy model included for demonstration.
- Includes test client with mock image data.
- Requires TensorFlow, grpcio, and related packages.

## Build and Run Instructions

### Rust Module

```bash
cd agriml_system/rust_edge
cargo build
cargo run
```

### C++ Module

```bash
cd agriml_system/cpp_weather
mkdir build && cd build
cmake ..
make
./weather_processing
```

### Python Module

```bash
cd agriml_system/python_ai
pip install -r requirements.txt
python crop_disease_detection.py
```

## Testing

- Rust: `cargo test` in `rust_edge` folder.
- C++: Run `weather_processing_test` executable.
- Python: Run `python test_crop_disease_detection.py`.

## Extensibility

- Protobuf definitions can be extended for additional data types and services.
- AI model in Python can be replaced with a trained Keras model.
- Rust and C++ modules can be extended for additional sensors and decision logic.

## Notes

- All components communicate via gRPC on different ports.
- Designed for lightweight, real-time field use.
- Modular and production-ready for easy integration and extension.
