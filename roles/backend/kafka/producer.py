from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers="10.0.0.21:9092")

topic = "demo-topic"

for i in range(5):
    message = f"Message {i}".encode("utf-8")
    producer.send(topic, value=message)

producer.flush()
producer.close()
