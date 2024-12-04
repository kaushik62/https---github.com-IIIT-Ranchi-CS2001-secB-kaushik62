import pandas as pd
import numpy as np

file_path = "AQI_Data.csv"
aqi_data = pd.read_csv(file_path)

print("First 8 rows of the dataset:")
print(aqi_data.head(8))

print("\nLast 5 rows of the dataset:")
print(aqi_data.tail(5))
print("\nDataset info:")
print(aqi_data.info())

city_stats = aqi_data.groupby("City").agg({
    "AQI": "mean",
    "PM2.5": "max",
    "PM10": "min"
}).reset_index()
print("\nCity-wise statistics:")
print(city_stats)

aqi_data.rename(columns={
    "AQI": "Air Quality Index",
    "PM2.5": "Particulate Matter 2.5",
    "PM10": "Particulate Matter 10",
    "City": "London"
}, inplace=True)

aqi_data["London"] = aqi_data["London"].replace("Unknown", "Not Available")

print("\nUpdated dataset:")
print(aqi_data.head())

result_file_path = "result.csv"
aqi_data.to_csv(result_file_path, index=False)
print(f"\nThe updated dataset has been saved to '{result_file_path}'.")
