import sqlite3
import os

# Ensure the backend folder exists
db_path = os.path.join(os.path.dirname(__file__), "skin_cancer.db")
conn = sqlite3.connect(db_path)

cursor = conn.cursor()

# Create a table for skin cancer data
cursor.execute('''
CREATE TABLE IF NOT EXISTS skin_cancer_trend (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    year INTEGER,
    cases INTEGER
)
''')

# Sample data for skin cancer trends (modify as needed)
data = [
    (2015, 1200),
    (2016, 1350),
    (2017, 1400),
    (2018, 1500),
    (2019, 1600),
    (2020, 1750),
    (2021, 1800),
]

# Insert data into table
cursor.executemany("INSERT INTO skin_cancer_trend (year, cases) VALUES (?, ?)", data)

# Commit and close the connection
conn.commit()
conn.close()

print("Database setup complete! 🎉")
