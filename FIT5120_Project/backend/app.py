from flask import Flask, jsonify
from flask_cors import CORS
import sqlite3
import matplotlib
matplotlib.use('Agg')  # Use a non-GUI backend
import matplotlib.pyplot as plt
import pandas as pd
import os

app = Flask(__name__)
CORS(app)  # Allow Vue.js frontend to call this API

DATABASE = "skin_cancer.db"

# Fetch data from SQLite
def get_data():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT year, cases FROM skin_cancer_trend ORDER BY year ASC")
    data = cursor.fetchall()
    conn.close()
    return [{"year": row[0], "cases": row[1]} for row in data]

# API Route: Get Skin Cancer Trend Data
@app.route("/api/skin_cancer_trends", methods=["GET"])
def skin_cancer_trends():
    data = get_data()
    return jsonify({"status": "success", "data": data})

# API Route: Generate and return a graph
@app.route("/api/generate_graph", methods=["GET"])
def generate_graph():
    data = get_data()
    
    if not data:
        return jsonify({"status": "error", "message": "No data found"}), 404

    # Convert to DataFrame
    df = pd.DataFrame(data)
    
    # Create graph
    plt.figure(figsize=(8,5))
    plt.plot(df["year"], df["cases"], marker="o", linestyle="-", color="red")
    plt.xlabel("Year")
    plt.ylabel("Number of Cases")
    plt.title("Skin Cancer Trends Over the Years")
    plt.grid(True)
    
    # Ensure 'static/' directory exists
    static_dir = "static"
    if not os.path.exists(static_dir):
        os.makedirs(static_dir)

    # Save graph in static folder
    graph_path = os.path.join(static_dir, "skin_cancer_trend.png")
    plt.savefig(graph_path)
    plt.close()  # Close the plot to free memory

    return jsonify({"status": "success", "graph_url": f"/{graph_path}"})

if __name__ == "__main__":
    app.run(debug=True)
