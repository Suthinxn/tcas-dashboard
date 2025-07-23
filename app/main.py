# Import packages
from dash import Dash, html, dash_table, dcc
import pandas as pd
import plotly.graph_objects as go

# Incorporate data
data = pd.read_csv("data/filtered_ai_com_courses.csv")

# Initialize the app
app = Dash()

# Create scatter map figure
def create_scatter_map(df):
    # สร้าง scatter map
    fig = go.Figure(go.Scattermap(
        lat=df['latitude'],  # แทนที่ด้วยชื่อคอลัมน์ latitude ของคุณ
        lon=df['longitude'],  # แทนที่ด้วยชื่อคอลัมน์ longitude ของคุณ
        mode='markers',
        marker=go.scattermap.Marker(
            size=12,
            color='red',
            opacity=0.7
        ),
        text=df['university_name_th'],  # แทนที่ด้วยชื่อคอลัมน์ชื่อมหาวิทยาลัยของคุณ
        hovertemplate='<b>%{text}</b><br>' +
                      'Latitude: %{lat}<br>' +
                      'Longitude: %{lon}<br>' +
                      '<extra></extra>'
    ))

    # ตั้งค่า layout สำหรับประเทศไทย
    fig.update_layout(
        autosize=True,
        hovermode='closest',
        map=dict(
            bearing=0,
            center=dict(
                lat=13.7563,  # กรุงเทพฯ
                lon=100.5018  # กรุงเทพฯ
            ),
            pitch=0,
            zoom=5.5,  # ซูมให้เห็นประเทศไทยทั้งหมด
            style='open-street-map'  # ใช้ OpenStreetMap
        ),
        height=600,
        margin=dict(r=0, t=0, l=0, b=0)
    )
    
    return fig

# App layout
app.layout = [
    html.Div([
        html.Div([
            html.H1("TCAS-DASHBOARD", style={"text-align": "center"})
        ]),
        html.Div([
            html.H2("Universities Location Map", style={"text-align": "center"}),
            dcc.Graph(figure=create_scatter_map(data))
        ]),
        # html.Div([
        #     html.H2("University Acceptance Data"),
        #     dcc.Graph(figure=px.histogram(data, x='university_name_th', y='number_acceptance_mko2'))
        # ])
    ])
]

# Run the app
if __name__ == '__main__':
    app.run(debug=True)