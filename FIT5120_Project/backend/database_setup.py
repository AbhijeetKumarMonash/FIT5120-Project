import sqlite3
import pandas as pd

# Define the dataset path
CSV_FILE_PATH = "C:/Users/Abhijeet/FIT5120-Project/FIT5120_Project/backend/df_melanoma.csv"
DATABASE_PATH = "C:/Users/Abhijeet/FIT5120-Project/FIT5120_Project/backend/skin_cancer.db"

# Connect to SQLite
conn = sqlite3.connect(DATABASE_PATH)
cursor = conn.cursor()

# 🚀 Drop table if it exists (this will erase existing data)
cursor.execute("DROP TABLE IF EXISTS melanoma_cases")

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS melanoma_cases (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Year INTEGER,
    StateOrTerritory TEXT,
    Count INTEGER
)
''')

# Read CSV and insert data into the table
df = pd.read_csv(CSV_FILE_PATH)

# Remove 'Australia' data
df = df[df['State or Territory'] != 'Australia']

# Insert data
for _, row in df.iterrows():
    cursor.execute("INSERT INTO melanoma_cases (Year, StateOrTerritory, Count) VALUES (?, ?, ?)", 
                   (row["Year"], row["State or Territory"], row["Count"]))

# Commit changes and close connection
conn.commit()
conn.close()

print("Database setup complete! 🎉")
