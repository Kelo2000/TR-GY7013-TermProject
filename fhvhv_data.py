import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# 1. Load data
# -----------------------------
df = pd.read_parquet("fhvhv_tripdata_2025-07.parquet")

# Normalize column names (all lowercase)
df.columns = df.columns.str.lower()

print("Data shape:", df.shape)
print("Columns:", df.columns)



################TO BE USED FOR GENERIC FHV DATA ANALYSIS#################
# -----------------------------
# 2. Parse datetime columns
# -----------------------------
# df["pickup_datetime"] = pd.to_datetime(df["pickup_datetime"])
# df["dropoff_datetime"] = pd.to_datetime(df["dropoff_datetime"])


# # Compute trip duration in minutes
# df["trip_duration_min"] = (df["dropoff_datetime"] - df["pickup_datetime"]).dt.total_seconds() / 60

# -----------------------------
# 3. Save first 2000 rows only
# -----------------------------
# df_sample = df.head(1000)
df.to_csv("fhvhv_tripdata_2025-07.csv", index=False)

print("✅ Saved first 1000 samples to fhv_tripdata_2025-07-sample.csv")

# -----------------------------
# 4. Quick Visualizations
# -----------------------------

# # Histogram of trip durations
# plt.figure(figsize=(8,5))
# sns.histplot(df_sample["trip_duration_min"], bins=40, kde=False)
# plt.title("Distribution of Trip Durations (sample of 1000)")
# plt.xlabel("Minutes")
# plt.ylabel("Count")
# plt.show()

# # Demand over hours of the day
# df_sample["hour"] = df_sample["pickup_datetime"].dt.hour
# plt.figure(figsize=(8,5))
# sns.countplot(x="hour", data=df_sample, palette="viridis")
# plt.title("Trip Requests by Hour of Day (sample of 1000)")
# plt.xlabel("Hour of Day")
# plt.ylabel("Number of Trips")
# plt.show()

# # Pickup vs Dropoff Location IDs (top 10)
# plt.figure(figsize=(10,5))
# df_sample["pulocationid"].value_counts().head(10).plot(kind="bar")
# plt.title("Top 10 Pickup Locations (sample of 1000)")
# plt.xlabel("Zone ID")
# plt.ylabel("Count")
# plt.show()


# ################################TO SEE DESTRIBUTION OF WAIT TIMES PER PICKUP ZONE##########################
# # Convert request_datetime to datetime format
# df["request_datetime"] = pd.to_datetime(df["request_datetime"])

# # Calculate waiting time in minutes (pickup_datetime - request_datetime)
# df["waiting_time_min"] = (df["pickup_datetime"] - df["request_datetime"]).dt.total_seconds() / 60

# # Filter out negative waiting times (if any)
# df = df[df["waiting_time_min"] >= 0]

# # Aggregate to find average waiting time by pickup zone
# zone_waiting_times = df.groupby("pulocationid")["waiting_time_min"].mean().sort_values()

# # Identify zones with highest and lowest average waiting time
# lowest_waiting_zone = zone_waiting_times.idxmin()
# highest_waiting_zone = zone_waiting_times.idxmax()

# print(f"Lowest avg waiting time zone: {lowest_waiting_zone} with {zone_waiting_times.min():.2f} min")
# print(f"Highest avg waiting time zone: {highest_waiting_zone} with {zone_waiting_times.max():.2f} min")

# # Plot histogram of waiting times
# plt.figure(figsize=(8,5))
# sns.histplot(df["waiting_time_min"], bins=50, kde=False)
# plt.title("Distribution of Waiting Times (Request to Pickup)")
# plt.xlabel("Waiting Time (minutes)")
# plt.ylabel("Count")
# plt.show()

# # Plot bar plots for top 10 zones with lowest and highest average waiting times
# plt.figure(figsize=(10,5))
# sns.barplot(x=zone_waiting_times.head(10).index.astype(str), y=zone_waiting_times.head(10).values, palette="Blues_r")
# plt.title("Top 10 Pickup Zones with Lowest Avg Waiting Time")
# plt.xlabel("PulocationID")
# plt.ylabel("Avg Waiting Time (min)")
# plt.show()

# plt.figure(figsize=(10,5))
# sns.barplot(x=zone_waiting_times.tail(10).index.astype(str), y=zone_waiting_times.tail(10).values, palette="Reds_r")
# plt.title("Top 10 Pickup Zones with Highest Avg Waiting Time")
# plt.xlabel("PulocationID")
# plt.ylabel("Avg Waiting Time (min)")
# plt.show()


##################################SPECIFIC TO VIA (HV0003) ONLY##################################

# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# # -----------------------------
# # 1. Load data
# # -----------------------------
# df = pd.read_parquet("fhvhv_tripdata_2024-02.parquet")

# # Normalize column names (all lowercase)
# df.columns = df.columns.str.lower()

# print("Data shape (full):", df.shape)
# print("Columns:", df.columns)

# # -----------------------------
# # 2. Filter only VIA (HV0004)
# # -----------------------------
# df_via = df[df["hvfhs_license_num"] == "HV0003"].copy()
# print("Data shape (Via only):", df_via.shape)

# # -----------------------------
# # 3. Parse datetime columns
# # -----------------------------
# df_via["pickup_datetime"] = pd.to_datetime(df_via["pickup_datetime"])
# df_via["dropoff_datetime"] = pd.to_datetime(df_via["dropoff_datetime"])

# # Compute trip duration in minutes
# df_via["trip_duration_min"] = (df_via["dropoff_datetime"] - df_via["pickup_datetime"]).dt.total_seconds() / 60

# # -----------------------------
# # 4. Save to CSV (sample of 1000 rows)
# # -----------------------------
# df_via_sample = df_via.head(1000)
# df_via_sample.to_csv("fhvhv_tripdata_2024-02-ubber_trips.csv", index=False)

# print("✅ Saved first 1000 VIA samples to fhvhv_tripdata_2024-02-via.csv")

# # -----------------------------
# # 5. Quick Visualizations
# # -----------------------------

# # Histogram of trip durations
# plt.figure(figsize=(8,5))
# sns.histplot(df_via_sample["trip_duration_min"], bins=40, kde=False)
# plt.title("Distribution of Trip Durations (VIA, sample of 1000)")
# plt.xlabel("Minutes")
# plt.ylabel("Count")
# plt.show()

# # Demand over hours of the day
# df_via_sample["hour"] = df_via_sample["pickup_datetime"].dt.hour
# plt.figure(figsize=(8,5))
# sns.countplot(x="hour", data=df_via_sample, palette="viridis")
# plt.title("Trip Requests by Hour of Day (VIA, sample of 1000)")
# plt.xlabel("Hour of Day")
# plt.ylabel("Number of Trips")
# plt.show()

# # Pickup vs Dropoff Location IDs (top 10)
# plt.figure(figsize=(10,5))
# df_via_sample["pulocationid"].value_counts().head(10).plot(kind="bar")
# plt.title("Top 10 Pickup Locations (VIA, sample of 1000)")
# plt.xlabel("Zone ID")
# plt.ylabel("Count")
# plt.show()
