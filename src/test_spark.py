from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

df = spark.read.csv("data.csv")

# BAD PRACTICE: collect on large dataset
data = df.collect()

for row in data:
    print(row)