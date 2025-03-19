import sqlite3
import pandas as pd


# Define the dataset path
CSV_FILE_PATH = "FIT5120_Project/backend/df_melanoma.csv"
DATABASE_PATH = "FIT5120_Project/backend/database_setup.py"

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

# only `Persons` 
df = df[(df['Sex'] == 'Persons') & (df['State or Territory'] != 'Australia')]

# insert
for _, row in df.iterrows():
    cursor.execute("INSERT INTO melanoma_cases (Year, StateOrTerritory, Count) VALUES (?, ?, ?)", 
                   (row["Year"], row["State or Territory"], row["Count"]))
    

# Commit changes and close connection
conn.commit()
conn.close()

print("Database setup complete! 🎉")

