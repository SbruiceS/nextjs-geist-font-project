// Kafka client integration for Rust edge module using rdkafka

use rdkafka::config::ClientConfig;
use rdkafka::producer::{FutureProducer, FutureRecord};
use rdkafka::consumer::{StreamConsumer, Consumer};
use rdkafka::message::Message;
use std::time::Duration;
use futures::StreamExt;

pub struct KafkaClient {
    producer: FutureProducer,
    consumer: StreamConsumer,
}

impl KafkaClient {
    pub fn new(brokers: &str, group_id: &str) -> KafkaClient {
        let producer: FutureProducer = ClientConfig::new()
            .set("bootstrap.servers", brokers)
            .create()
            .expect("Producer creation error");

        let consumer: StreamConsumer = ClientConfig::new()
            .set("group.id", group_id)
            .set("bootstrap.servers", brokers)
            .set("enable.partition.eof", "false")
            .set("session.timeout.ms", "6000")
            .set("enable.auto.commit", "true")
            .create()
            .expect("Consumer creation failed");

        KafkaClient { producer, consumer }
    }

    pub async fn send_message(&self, topic: &str, payload: &str) {
        let record = FutureRecord::to(topic)
            .payload(payload)
            .key("");
        let _ = self.producer.send(record, Duration::from_secs(0)).await;
    }

    pub async fn consume_messages(&self, topic: &str) {
        self.consumer.subscribe(&[topic]).expect("Subscription failed");
        let mut message_stream = self.consumer.stream();

        while let Some(message) = message_stream.next().await {
            match message {
                Ok(m) => {
                    if let Some(payload) = m.payload_view::<str>().unwrap_or(None) {
                        println!("Received message: {}", payload);
                    }
                }
                Err(e) => eprintln!("Kafka error: {}", e),
            }
        }
    }
}
