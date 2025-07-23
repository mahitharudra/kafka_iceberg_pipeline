# Kafka to Iceberg Streaming Pipeline

This project demonstrates an end-to-end pipeline reading JSON messages from Kafka,
parsing and writing them in real-time to an Apache Iceberg table using Spark Structured Streaming.

## Components

- **Kafka + Zookeeper**: Containerized using Docker Compose.
- **Spark Structured Streaming**: Reads Kafka topic `sales` and writes to Iceberg.
- **Iceberg**: Stores data files and metadata on local filesystem (configurable).

## How to Run

1. Start Kafka cluster:

```bash
cd docker
docker-compose up -d
```

2. Run streaming job:

```bash
spark-submit \
  --packages org.apache.iceberg:iceberg-spark-runtime-3.4_2.12:1.3.1 \
  scripts/streaming_pipeline.py
```

3. Produce test data:

```bash
python3 scripts/produce_messages.py
```

4. Query Iceberg data:

```bash
spark-submit \
  --packages org.apache.iceberg:iceberg-spark-runtime-3.4_2.12:1.3.1 \
  scripts/read_iceberg.py
```

## Folder Structure

```
kafka-iceberg-pipeline/
├── README.md
├── docker/
│   └── docker-compose.yml
├── scripts/
│   ├── produce_messages.py
│   ├── read_iceberg.py
│   └── streaming_pipeline.py
└── requirements.txt
```

---

Feel free to extend and customize this project!
