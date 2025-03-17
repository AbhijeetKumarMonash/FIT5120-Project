import sqlite3
import pandas as pd
import glob
import os

# Define the database path
DATABASE_PATH = "C:/Users/Abhijeet/FIT5120-Project/FIT5120_Project/backend/skin_cancer.db"
DATA_FOLDER = "C:/Users/Abhijeet/FIT5120-Project/FIT5120_Project/backend/data_uv_index"

# Connect to SQLite
conn = sqlite3.connect(DATABASE_PATH)
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS uv_index_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    location TEXT,
    month INTEGER,
    uv_index REAL
)
''')

# Define regions
regions = ["act", "nsw", "nt", "qld", "sa", "tas", "vic", "wa"]

# Process CSV files for each region
dfs = []
for region in regions:
    files = glob.glob(f"{DATA_FOLDER}/{region}*.csv")  # Get all CSV files for the region
    
    if not files:
        print(f"⚠️ No CSV files found for region: {region}")
        continue  # Skip this region if no files found

    region_df = []
    for file in files:
        print(f"📂 Processing file: {file}")
        df = pd.read_csv(file)  # Read CSV
        if 'Date-Time' not in df.columns or 'UV_Index' not in df.columns:
            print(f"❌ Skipping file {file} - Missing expected columns")
            continue  # Skip files with missing columns

        df['Date-Time'] = pd.to_datetime(df['Date-Time'], errors='coerce')  # Convert to datetime
        df = df.dropna(subset=['Date-Time'])  # Remove invalid dates
        df['month'] = df['Date-Time'].dt.month  # Extract the month
        region_df.append(df)

    # Combine all data for the region
    if region_df:
        full_df = pd.concat(region_df, ignore_index=True)
        avg_uv = full_df.groupby('month')['UV_Index'].mean().reset_index()
        avg_uv['location'] = region.upper()  # Assign region name
        dfs.append(avg_uv)
    else:
        print(f"⚠️ No valid data for region: {region}")

# Merge all data and insert into database
if dfs:
    uv_all = pd.concat(dfs)
    for _, row in uv_all.iterrows():
        cursor.execute("INSERT INTO uv_index_data (location, month, uv_index) VALUES (?, ?, ?)",
                       (row["location"], row["month"], row["UV_Index"]))

    # Commit changes and close connection
    conn.commit()
    print("✅ UV Index Database Created Successfully!")
else:
    print("❌ No valid data to insert into the database.")

conn.close()
