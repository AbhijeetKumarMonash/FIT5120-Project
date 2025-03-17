from flask import Flask, jsonify,send_file
from flask_cors import CORS
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os

app = Flask(__name__)
CORS(app)  # Allow Vue.js frontend to call this API

DATABASE_PATH = "C:/Users/Abhijeet/FIT5120-Project/FIT5120_Project/backend/skin_cancer.db"

STATIC_DIR = "static"
HEATMAP_PATH = os.path.join(STATIC_DIR, "uv_index_heatmap.png")


# Fetch data from SQLite
def get_data_from_db():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    
    # Fetch year, state, and case count
    cursor.execute("SELECT Year, StateOrTerritory, Count FROM melanoma_cases ORDER BY Year ASC")
    data = cursor.fetchall()
    
    conn.close()

    # Convert to list of dictionaries
    return [{"Year": row[0], "State or Territory": row[1], "Count": row[2]} for row in data]

@app.route("/api/uv_index_trends", methods=["GET"])
def generate_uv_heatmap():
    # Connect to database
    conn = sqlite3.connect(DATABASE_PATH)
    
    query = """
    SELECT month, location, AVG(uv_index) AS AvgUV 
    FROM uv_index_data 
    GROUP BY month, location
    """
    
    df = pd.read_sql_query(query, conn)
    conn.close()

    # Pivot table: location as index, month as columns
    heatmap_data = df.pivot(index="location", columns="month", values="AvgUV")

    # Generate heatmap
    plt.figure(figsize=(12, 6))
    sns.heatmap(heatmap_data, cmap="coolwarm", annot=True, fmt=".2f", linewidths=0.5)

    # Set title and labels
    plt.title("Average Monthly UV Index (2018-2020) - Australian States & Territories")
    plt.xlabel("Month")
    plt.ylabel("Location")

    # Save heatmap image
    plt.savefig(HEATMAP_PATH)
    plt.close()

    # ✅ Ensure the path is correctly formatted for the frontend
    graph_url = HEATMAP_PATH.replace("\\", "/")  # Replace backslashes with forward slashes

    return jsonify({"status": "success", "graph_url": f"http://127.0.0.1:5000/{graph_url}"})



# API Route to fetch skin cancer data and generate a Plotly line chart
@app.route("/api/skin_cancer_trends", methods=["GET"])
def generate_plotly_graph():
    # Fetch data from the database
    data = get_data_from_db()
    if not data:
        return jsonify({"status": "error", "message": "No data found"}), 404

    # Convert to Pandas DataFrame
    df = pd.DataFrame(data)

    # Filter out 'Australia' from 'State or Territory'
    df_filtered = df[df['State or Territory'] != 'Australia']

    # Define custom colors for each state/territory
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

    # Create an interactive line chart using Plotly
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

    # Ensure x-axis shows every 3 years
    years = sorted(df_filtered['Year'].unique())  
    fig.update_xaxes(tickmode='array', tickvals=years[::3])

    # Set y-axis tick spacing to 1000
    fig.update_yaxes(dtick=1000)

    # Ensure 'static/' directory exists
    static_dir = "static"
    if not os.path.exists(static_dir):
        os.makedirs(static_dir)

    # Save Plotly figure as an HTML file
    graph_html_path = os.path.join(static_dir, "skin_cancer_trend.html")
    fig.write_html(graph_html_path)

    return jsonify({"status": "success", "graph_url": f"http://127.0.0.1:5000/{graph_html_path}"})

if __name__ == "__main__":
    app.run(debug=True)
