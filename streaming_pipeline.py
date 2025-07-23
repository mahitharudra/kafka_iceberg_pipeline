from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StringType, DoubleType

schema = StructType() \
    .add("id", StringType()) \
    .add("product", StringType()) \
    .add("amount", DoubleType()) \
    .add("sale_date", StringType())

spark = SparkSession.builder \
    .appName("KafkaToIcebergStream") \
    .config("spark.sql.catalog.my_catalog", "org.apache.iceberg.spark.SparkCatalog") \
    .config("spark.sql.catalog.my_catalog.type", "hadoop") \
    .config("spark.sql.catalog.my_catalog.warehouse", "/Users/mahithaadigoppula/Documents/iceberg_warehouse") \
    .getOrCreate()

kafka_df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "sales") \
    .option("startingOffsets", "earliest") \
    .load()

value_df = kafka_df.selectExpr("CAST(value AS STRING)") \
    .select(from_json(col("value"), schema).alias("data")) \
    .select("data.*") \
    .withColumn("sale_date", col("sale_date").cast("date"))

query = value_df.writeStream \
    .format("iceberg") \
    .outputMode("append") \
    .option("checkpointLocation", "/tmp/checkpoint/sales") \
    .start("my_catalog.default.sales_stream")

query.awaitTermination()
