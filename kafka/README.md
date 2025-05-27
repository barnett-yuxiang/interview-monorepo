**Kafka Setup Guide**
Three steps:
1. Start Kafka using Docker and create a topic.
2. Start the consumer.
3. Start the producer.

It is recommended to use Wurstmeister's Kafka images, which support rapid deployment of ZooKeeper and Kafka.
```
docker pull wurstmeister/kafka
docker pull wurstmeister/zookeeper
```

Use `docker-compose up -d` in the `kafka` directory, and `docker-compose ps` to check the status.

Create a Topic in the Kafka container:
```
docker exec -it projects-kafka-1 '/opt/kafka/bin/kafka-topics.sh' --create --topic demo-topic --bootstrap-server <HOST_IP>:9092 --partitions 1 --replication-factor 1
```
