from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("ReadIceberg") \
    .config("spark.sql.catalog.my_catalog", "org.apache.iceberg.spark.SparkCatalog") \
    .config("spark.sql.catalog.my_catalog.type", "hadoop") \
    .config("spark.sql.catalog.my_catalog.warehouse", "/Users/mahithaadigoppula/Documents/iceberg_warehouse") \
    .getOrCreate()

df = spark.read.format("iceberg").load("my_catalog.default.sales_stream")
df.show()

spark.stop()
