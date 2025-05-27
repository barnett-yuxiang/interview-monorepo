from kafka import KafkaConsumer

consumer = KafkaConsumer(
    "demo-topic",
    bootstrap_servers="10.0.0.21:9092",
    auto_offset_reset="earliest",
    group_id="my-group",
)

for record in consumer:
    print(f"Received: {record.value.decode('utf-8')}")
