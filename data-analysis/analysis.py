import matplotlib
matplotlib.use('Agg')  # Use non-GUI backend to avoid Tkinter errors

import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the dataset
file_path = "air_quality.csv"  # Update with your dataset file name if different
df = pd.read_csv(file_path)

# Step 2: Display first 5 rows
print("\nFirst 5 rows of the dataset:")
print(df.head())

# Step 3: Dataset info
print("\nDataset Info:")
print(df.info())

# Step 4: Missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# Step 5: Summary statistics
print("\nSummary statistics:")
print(df.describe())

# Step 6: Plot AQI over time
plt.figure(figsize=(10, 5))
plt.plot(df['AQI'], label='AQI')
plt.title("AQI over Time")
plt.xlabel("Days")
plt.ylabel("AQI")
plt.legend()
plt.savefig("aqi_over_time.png")
plt.close()

# Step 7: Correlation heatmap
plt.figure(figsize=(8, 6))
correlation = df.corr(numeric_only=True)
plt.imshow(correlation, cmap='coolwarm', interpolation='nearest')
plt.colorbar()
plt.xticks(range(len(correlation.columns)), correlation.columns, rotation=90)
plt.yticks(range(len(correlation.columns)), correlation.columns)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("correlation_heatmap.png")
plt.close()

# Step 8: PM2.5 vs AQI scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(df['PM2.5'], df['AQI'], alpha=0.5)
plt.title("PM2.5 vs AQI")
plt.xlabel("PM2.5")
plt.ylabel("AQI")
plt.savefig("pm25_vs_aqi.png")
plt.close()

# Step 9: AQI distribution
plt.figure(figsize=(8, 6))
plt.hist(df['AQI'], bins=30, color='skyblue', edgecolor='black')
plt.title("AQI Distribution")
plt.xlabel("AQI")
plt.ylabel("Frequency")
plt.savefig("aqi_distribution.png")
plt.close()

print("\n✅ Analysis completed. All plots saved as PNG files in the project folder.")
