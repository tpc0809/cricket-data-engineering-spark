from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Initialize Spark Session
spark = SparkSession.builder.appName("CricketAnalysis").getOrCreate()
spark.conf.set("spark.sql.debug.maxToStringFields", 100)

# Load dataset
file_path = "Cricket_Dataset_Players.csv"
df = spark.read.option("header", True).csv(file_path)

# Show available columns
print("\nColumns in dataset:", df.columns)

# Initial Data Preview - Show first 25 rows (ensuring full display)
print("\nInitial Data Preview:")
df.show(25, truncate=False)

# Selecting relevant columns and renaming them
df_cleaned = df.select(
    col("Player Name").alias("player_name"),
    col("Country").alias("country"),
    col("Years Active").alias("years_active"),
    col("Matches").cast("int"),
    col("Innings").cast("int"),
    col("Not Outs").cast("int"),
    col("Runs").cast("int"),
    col("High Score").alias("high_score"),
    col("Batting Average").cast("double"),
    col("Hundreds").cast("int"),
    col("Fifties").cast("int"),
    col("Ducks").cast("int"),
    col("Batting Strike Rate").cast("double"),
    col("Balls Faced").cast("int"),
    col("Boundary %").alias("boundary_percentage").cast("double"),
    col("Sixes Hit").alias("sixes_hit").cast("int"),
    col("Fours Hit").alias("fours_hit").cast("int"),
    col("Consistency Score").cast("double"),
    col("Player Impact Score").cast("double"),
    col("Man of the Match Awards").alias("man_of_the_match_awards").cast("int"),
    col("Catches Taken").alias("catches_taken").cast("int"),
    col("Stumpings").cast("int"),
    col("Run Outs").alias("run_outs").cast("int"),
    col("Matches Won Contribution (%)").alias("matches_won_contribution").cast("double"),
    col("Bowling Wickets").alias("wickets").cast("int"),
    col("Bowling Average").cast("double"),
    col("Bowling Economy Rate").cast("double"),
    col("Bowling Strike Rate").cast("double"),
    col("Best Bowling Figures").alias("best_bowling_figures"),
    col("Overs Bowled").cast("int"),
    col("Five-Wicket Hauls").alias("five_wicket_hauls").cast("int"),
    col("Ten-Wicket Hauls").alias("ten_wicket_hauls").cast("int")
)

# Show cleaned data preview - 25 rows
print("\nCleaned Data Preview:")
df_cleaned.show(25, truncate=False)

# Show schema of cleaned data
print("\nSchema of Cleaned Data:")
df_cleaned.printSchema()

# Show summary statistics
print("\nSummary Statistics:")
df_cleaned.describe().show()
