📌 Project Overview
This project focuses on analyzing an air quality dataset containing daily pollution measurements and AQI values.
The dataset includes various pollutants, temporal features, and holiday information.
The objective is to clean, analyze, and visualize the data to identify trends, patterns, and correlations.

📂 Dataset Description
The dataset (air_quality.csv) contains the following features:

Pollutants: PM2.5, PM10, NO₂, SO₂, CO, Ozone

Time Features: Date, Month, Year, Days (numeric representation of day)

Holiday Information:

1 → Holiday

0 → Working day

Target Variable: AQI (Air Quality Index)

🛠️ Technologies Used
Python 3

Pandas – Data manipulation and cleaning

Matplotlib & Seaborn – Data visualization

⚙️ Project Setup
Create Project Folder
Create a folder data-analysis inside the DAY 5 directory.

Create Virtual Environment

python -m venv data-analysis

Activate Virtual Environment

.\data-analysis\Scripts\activate

Install Required Libraries

pip install pandas matplotlib seaborn

Add Dataset
Place air_quality.csv inside the project folder.

📜 Analysis Steps
Step 1 – Understanding the Task
The objective of this task was to perform data analysis on an air quality dataset containing daily pollution measurements such as PM2.5, PM10, NO₂, SO₂, CO, Ozone, and AQI values.
The dataset also had temporal features (Date, Month, Year, Days) and holiday information (1 for holiday, 0 for working day).
The main goal was to clean, analyze, and visualize this data to understand trends and patterns.

Step 2 – Loading and Inspecting Data
Load dataset using Pandas.

Display the first 5 rows to verify correct loading.

Check dataset information (df.info()), missing values, and summary statistics.

Step 3 – Data Visualization
Generated the following plots:

Line Plot – AQI over time

Box Plot – AQI distribution by month

Heatmap – Correlation between pollutants and AQI

All plots are saved as .png files in the project folder instead of showing them directly to avoid Tkinter-related display errors.

▶️ Running the Analysis
Run the script:

python analysis.py

The terminal output includes:

Dataset information (.info())

Missing values report

Summary statistics

The analysis also saves visualizations in PNG format in the project folder.

📊 Output Files
The script generates the following output files:

aqi_trend.png – AQI over time

aqi_monthly_distribution.png – AQI distribution per month

pollutants_aqi_correlation.png – Correlation heatmap

📌 Key Insights
AQI shows noticeable seasonal changes over months.

Certain pollutants have strong correlations with AQI.

Holiday vs. working days may impact AQI readings.
