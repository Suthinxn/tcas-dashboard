# Import packages
from dash import Dash, html, dash_table, dcc
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# Incorporate data
data = pd.read_csv("data/filtered_ai_com_courses.csv")


external_stylesheets = [
    "https://cdn.jsdelivr.net/npm/daisyui@3.7.6/dist/full.css"
]

# Initialize the app
# app = Dash()
app = Dash(__name__, external_stylesheets=external_stylesheets)

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
app.layout = html.Div([
    html.Div([
        html.Div([
            html.Div([
                html.Div("🎓 TCAS68 Dashboard", style={"fontSize": "2rem", "fontWeight": "bold"})
            ], className="navbar-start"),
            html.A(
                html.Button("Go to TCAS", className="btn btn-neutral"), href="https://mytcas.com/", 
                target="_blank",
                className="navbar-end")
        ], className="navbar bg-base-200 shadow-sm")
    ]),

    html.Div([
        html.Div([

        # ฝั่งซ้าย: แผนที่
        html.Div([
            html.H2("🌍 Universities Location Map", style={
                "fontSize": "1.25rem",
                "fontWeight": "600",
                "marginBottom": "1rem",
                "textAlign": "center"
            }),
            dcc.Graph(figure=create_scatter_map(data), style={"width": "100%"})
        ], style={
            "width": "50%",
            "height": "50%",
            "background": "#fff",
            "boxShadow": "0 2px 8px #e5e7eb",
            "padding": "1.5rem"
        }),

        # ฝั่งขวา: สอง histogram ซ้อนกันแนวตั้ง
        html.Div([
            html.H2("📊 University Acceptance Data", style={
                "fontSize": "1.25rem",
                "fontWeight": "600",
                "marginBottom": "1rem"
            }),
            dcc.Graph(
                figure=px.histogram(data, x='university_name_th', y='number_acceptance_mko2'),
                style={"height": "45%"}
            ),

            html.H2("📊 University Acceptance Data 2", style={
                "fontSize": "1.25rem",
                "fontWeight": "600",
                "marginBottom": "1rem",
                "marginTop": "2rem"
            }),
            dcc.Graph(
                figure=px.histogram(data, x='university_name_th', y='number_acceptance_mko2'),
                style={"height": "45%"}
            )
        ], style={
            "height": "92vh",      # เท่ากับ map
            "width": "50%",
            "background": "#fff",
            "boxShadow": "0 2px 8px #e5e7eb",
            "padding": "1.5rem",
            "display": "flex",
            "flexDirection": "column",
            "justifyContent": "space-between"
        }),
        ], style={"display": "flex", "width": "100%"}),


        html.Div([
            html.Div([
                html.H2("📊 University Acceptance Data", className="text-xl font-semibold mb-4"),
                dcc.Graph(figure=px.histogram(data, x='university_name_th', y='number_acceptance_mko2'))
            ], className="card bg-base-100 shadow-xl p-6")

        ], className="w-full lg:w-1/2 p-4")
    ], className="flex flex-wrap justify-center")
], className="container mx-auto py-4")

# Run the app
if __name__ == '__main__':
    app.run(debug=True)