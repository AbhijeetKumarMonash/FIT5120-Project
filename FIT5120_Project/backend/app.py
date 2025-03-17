from flask import Flask, jsonify
from flask_cors import CORS
import sqlite3
import pandas as pd
import plotly.express as px
import os

app = Flask(__name__)
CORS(app)  # Allow Vue.js frontend to call this API

DATABASE_PATH = "C:/Users/Abhijeet/FIT5120-Project/FIT5120_Project/backend/skin_cancer.db"

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
