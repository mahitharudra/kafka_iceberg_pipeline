from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

test_messages = [
    {"id": "101", "product": "Tablet", "amount": 299.99, "sale_date": "2025-07-23"},
    {"id": "102", "product": "Mouse", "amount": 25.99, "sale_date": "2025-07-23"},
    {"id": "103", "product": "laptop", "amount": 32.99, "sale_date": "2024-07-23"},
]

if __name__ == "__main__":
    for msg in test_messages:
        producer.send('sales', msg)
        print(f"Sent: {msg}")
        time.sleep(1)
    producer.flush()
