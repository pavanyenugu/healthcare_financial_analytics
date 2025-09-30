from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when

# Initialize Spark
spark = SparkSession.builder \
    .appName("HealthcareETL") \
    .getOrCreate()

# Load data
pharmacy = spark.read.csv("data/pharmacy.csv", header=True, inferSchema=True)
lab = spark.read.csv("data/lab.csv", header=True, inferSchema=True)
eligibility = spark.read.csv("data/eligibility.csv", header=True, inferSchema=True)

# Example transformations
pharmacy = pharmacy.withColumn("drug_cost", col("quantity") * col("unit_price"))
lab = lab.filter(col("result_flag") == "ABNORMAL")

# Join datasets
combined = eligibility.join(pharmacy, "patient_id", "left") \
                      .join(lab, "patient_id", "left")

# Save as parquet (optimized format)
combined.write.mode("overwrite").parquet("output/healthcare_data.parquet")

print("ETL Pipeline completed. Data saved in output/")
spark.stop()
