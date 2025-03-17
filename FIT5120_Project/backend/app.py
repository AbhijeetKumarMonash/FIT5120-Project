from flask import Flask, jsonify, send_file, request
from flask_cors import CORS
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os

app = Flask(__name__)
CORS(app)

DATABASE_PATH = os.path.join(os.path.dirname(__file__), "skin_cancer.db")

STATIC_DIR = "static"
HEATMAP_PATH = os.path.join(STATIC_DIR, "uv_index_heatmap.png")

def get_data_from_db():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT Year, StateOrTerritory, Count FROM melanoma_cases ORDER BY Year ASC")
    data = cursor.fetchall()
    conn.close()
    return [{"Year": row[0], "State or Territory": row[1], "Count": row[2]} for row in data]

@app.route("/api/uv_index_trends", methods=["GET"])
def generate_uv_heatmap():
    conn = sqlite3.connect(DATABASE_PATH)
    query = """
    SELECT month, location, AVG(uv_index) AS AvgUV 
    FROM uv_index_data 
    GROUP BY month, location
    """
    df = pd.read_sql_query(query, conn)
    conn.close()

    heatmap_data = df.pivot(index="location", columns="month", values="AvgUV")
    plt.figure(figsize=(12, 6))
    sns.heatmap(heatmap_data, cmap="coolwarm", annot=True, fmt=".2f", linewidths=0.5)
    plt.title("Average Monthly UV Index (2018-2020) - Australian States & Territories")
    plt.xlabel("Month")
    plt.ylabel("Location")

    if not os.path.exists(STATIC_DIR):
        os.makedirs(STATIC_DIR)
    plt.savefig(HEATMAP_PATH)
    plt.close()

    base_url = request.url_root.rstrip("/")
    fixed_path = HEATMAP_PATH.replace("\\", "/")       # <-- FIX HERE
    graph_url = f"{base_url}/{fixed_path}"

    return jsonify({"status": "success", "graph_url": graph_url})

@app.route("/api/skin_cancer_trends", methods=["GET"])
def generate_plotly_graph():
    data = get_data_from_db()
    if not data:
        return jsonify({"status": "error", "message": "No data found"}), 404

    df = pd.DataFrame(data)
    df_filtered = df[df['State or Territory'] != 'Australia']

    color_map = {
        'New South Wales': 'red',
        'Australian Capital Territory': 'blue',
        'Northern Territory': 'green',
        'Queensland': 'black',
        'South Australia': 'orange',
        'Tasmania': 'darkviolet',  
        'Victoria': 'yellow',
        'Western Australia': 'purple'
    }

    fig = px.line(
        df_filtered, 
        x='Year', 
        y='Count', 
        color='State or Territory',
        markers=True,  
        title="Skin Cancer Trends Over Years In Australia",
        labels={'Year': 'Year', 'Count': 'Cancer Count'},
        hover_data={'Year': True, 'Count': True, 'State or Territory': True}, 
        color_discrete_map=color_map  
    )

    years = sorted(df_filtered['Year'].unique())
    fig.update_xaxes(tickmode='array', tickvals=years[::3])
    fig.update_yaxes(dtick=1000)

    if not os.path.exists(STATIC_DIR):
        os.makedirs(STATIC_DIR)
    graph_html_path = os.path.join(STATIC_DIR, "skin_cancer_trend.html")
    fig.write_html(graph_html_path)

    base_url = request.url_root.rstrip("/")
    fixed_path = graph_html_path.replace("\\", "/")    # <-- FIX HERE
    graph_url = f"{base_url}/{fixed_path}"

    return jsonify({"status": "success", "graph_url": graph_url})

@app.route("/", methods=["GET"])
def index():
    return "Hello from Flask!"

if __name__ == "__main__":
    app.run(debug=True)
