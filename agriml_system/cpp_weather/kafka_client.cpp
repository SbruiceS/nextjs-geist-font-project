// Kafka client integration for C++ weather module using librdkafka

#include <iostream>
#include <string>
#include <librdkafka/rdkafkacpp.h>

class KafkaClient {
public:
    KafkaClient(const std::string& brokers, const std::string& group_id) {
        std::string errstr;

        // Producer config
        RdKafka::Conf* conf = RdKafka::Conf::create(RdKafka::Conf::CONF_GLOBAL);
        conf->set("bootstrap.servers", brokers, errstr);

        producer_ = RdKafka::Producer::create(conf, errstr);
        if (!producer_) {
            std::cerr << "Failed to create producer: " << errstr << std::endl;
            exit(1);
        }

        // Consumer config
        RdKafka::Conf* tconf = RdKafka::Conf::create(RdKafka::Conf::CONF_TOPIC);
        consumer_conf_ = RdKafka::Conf::create(RdKafka::Conf::CONF_GLOBAL);
        consumer_conf_->set("group.id", group_id, errstr);
        consumer_conf_->set("bootstrap.servers", brokers, errstr);

        consumer_ = RdKafka::KafkaConsumer::create(consumer_conf_, errstr);
        if (!consumer_) {
            std::cerr << "Failed to create consumer: " << errstr << std::endl;
            exit(1);
        }
    }

    ~KafkaClient() {
        delete producer_;
        delete consumer_;
        delete consumer_conf_;
    }

    void send_message(const std::string& topic, const std::string& message) {
        RdKafka::ErrorCode resp = producer_->produce(
            topic, RdKafka::Topic::PARTITION_UA,
            RdKafka::Producer::RK_MSG_COPY,
            const_cast<char*>(message.c_str()), message.size(),
            nullptr, nullptr);

        if (resp != RdKafka::ERR_NO_ERROR) {
            std::cerr << "Failed to send message: " << RdKafka::err2str(resp) << std::endl;
        } else {
            producer_->poll(0);
        }
    }

    void consume_messages(const std::string& topic) {
        std::vector<std::string> topics = {topic};
        RdKafka::ErrorCode err = consumer_->subscribe(topics);
        if (err) {
            std::cerr << "Failed to subscribe to topic: " << RdKafka::err2str(err) << std::endl;
            return;
        }

        while (true) {
            RdKafka::Message* msg = consumer_->consume(1000);
            if (!msg) continue;

            switch (msg->err()) {
                case RdKafka::ERR__TIMED_OUT:
                    break;
                case RdKafka::ERR_NO_ERROR:
                    std::cout << "Received message: " << static_cast<const char*>(msg->payload()) << std::endl;
                    break;
                default:
                    std::cerr << "Consume failed: " << msg->errstr() << std::endl;
                    break;
            }
            delete msg;
        }
    }

private:
    RdKafka::Producer* producer_;
    RdKafka::KafkaConsumer* consumer_;
    RdKafka::Conf* consumer_conf_;
};
