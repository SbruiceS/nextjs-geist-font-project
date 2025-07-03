# Rust Edge Module Dockerfile
FROM rust:1.70 as builder

WORKDIR /usr/src/app

COPY ../../rust_edge/Cargo.toml .
COPY ../../rust_edge/Cargo.lock .
COPY ../../rust_edge/build.rs .
COPY ../../proto ./proto
COPY ../../rust_edge/src ./src

RUN cargo build --release

FROM debian:buster-slim

RUN apt-get update && apt-get install -y ca-certificates && rm -rf /var/lib/apt/lists/*

COPY --from=builder /usr/src/app/target/release/rust_edge /usr/local/bin/rust_edge

EXPOSE 50051

USER nobody

CMD ["rust_edge"]
