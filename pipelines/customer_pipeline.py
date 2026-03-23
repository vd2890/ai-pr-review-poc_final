from src.transformations.customer_transform import transform

def run_pipeline(spark):
    df = spark.read.parquet("/data/input")

    result = transform(df)

    for r in result:
        print(r)