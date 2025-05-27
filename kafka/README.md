**Kafka Setup Guide**
Three steps:
1. Start Kafka using Docker and create a topic.
2. Start the consumer.
3. Start the producer.

推荐使用 Wurstmeister 的 Kafka 镜像 ，它支持 ZooKeeper 和 Kafka 的快速部署
docker pull wurstmeister/kafka
docker pull wurstmeister/zookeeper

docker run -d \
  --name kafka \
  -p 9092:9092 \
  -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://<宿主机局域网IP>:9092 \
  -e KAFKA_LISTENERS=PLAINTEXT://0.0.0.0:9092 \
  -e KAFKA_ZOOKEEPER_CONNECT=zookeeper:2181 \
  --network host \
  wurstmeister/kafka

  在 Kafka 容器中创建一个 Topic：
  docker exec -it kafka \
  bin/kafka-topics.sh --create --topic demo-topic \
  --bootstrap-server <宿主机局域网IP>:9092 \
  --partitions 1 --replication-factor 1
