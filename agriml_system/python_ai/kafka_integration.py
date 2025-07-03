"""
Kafka integration module for Python AI services.
Provides Kafka producer and consumer for real-time data streaming.
"""

from kafka import KafkaProducer, KafkaConsumer
import json

class KafkaClient:
    def __init__(self, bootstrap_servers='localhost:9092'):
        self.producer = KafkaProducer(
            bootstrap_servers=bootstrap_servers,
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
        self.consumer = None
        self.bootstrap_servers = bootstrap_servers

    def send_message(self, topic, message):
        self.producer.send(topic, message)
        self.producer.flush()

    def start_consumer(self, topic, group_id='agriml-group'):
        self.consumer = KafkaConsumer(
            topic,
            bootstrap_servers=self.bootstrap_servers,
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id=group_id,
            value_deserializer=lambda m: json.loads(m.decode('utf-8'))
        )
        return self.consumer

    def consume_messages(self, topic, group_id='agriml-group'):
        consumer = self.start_consumer(topic, group_id)
        for message in consumer:
            yield message.value
