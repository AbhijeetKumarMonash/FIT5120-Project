import sqlite3

DATABASE_PATH = "C:/Users/Abhijeet/FIT5120-Project/FIT5120_Project/backend/skin_cancer.db"

conn = sqlite3.connect(DATABASE_PATH)
cursor = conn.cursor()

# Get the table schema
cursor.execute("PRAGMA table_info(uv_index_data);")
columns = cursor.fetchall()

# Print column names
for col in columns:
    print(col)

conn.close()
