# Import packages
from dash import Dash, html, dcc, Input, Output
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# Load data
data_location = pd.read_csv("data/filtered_ai_com_courses.csv")
data = pd.read_excel("data/final_filtered_ai_com_courses.xlsx")

# External stylesheets
external_stylesheets = [
    "https://cdn.jsdelivr.net/npm/daisyui@3.7.6/dist/full.css"
]

# Initialize Dash app
app = Dash(__name__, external_stylesheets=external_stylesheets)

# ===== Helper functions =====

def create_bar_cost(data):
    fig = px.bar(data, x='info', y='cost')
    fig.update_layout(
        xaxis_showticklabels=False,
        xaxis_title="ข้อมูลหลักสูตร",
        yaxis_title="ราคา (บาท)"
    )
    return fig

def create_bar_group(data):
    fig = px.histogram(data, x="university_name_th", color="field_name_en", barmode="group")
    fig.update_layout(
        xaxis_showticklabels=False,
        xaxis_title="มหาวิทยาลัย",
        yaxis_title="จำนวนหลักสูตร",
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="center",
            x=0.5
        )
    )
    return fig

def create_map_figure(selected_uni=None):
    df = data_location.copy()

    fig = go.Figure(go.Scattermapbox(
        lat=df['latitude'],
        lon=df['longitude'],
        mode='markers',
        marker=go.scattermapbox.Marker(size=12, color='red', opacity=0.7),
        text=df['university_name_th'],
        hovertemplate='<b>%{text}</b><br>Latitude: %{lat}<br>Longitude: %{lon}<extra></extra>'
    ))

    # Default: กรุงเทพ
    center_lat, center_lon, zoom = 13.7563, 100.5018, 5.5

    if selected_uni:
        selected = df[df['university_name_th'] == selected_uni]
        if not selected.empty:
            row = selected.iloc[0]
            center_lat, center_lon = row['latitude'], row['longitude']
            zoom = 12

    fig.update_layout(
        mapbox=dict(
            style="open-street-map",
            center=dict(lat=center_lat, lon=center_lon),
            zoom=zoom
        ),
        height=600,
        margin=dict(r=0, t=0, l=0, b=0)
    )

    return fig

# ===== App layout =====

app.layout = html.Div([
    # Top navbar
    html.Div([
        html.Div([
            html.Div("🎓 TCAS68 Dashboard", style={"fontSize": "2rem", "fontWeight": "bold"})
        ], className="navbar-start"),
        html.Div(
            html.A(
                html.Button("Go to TCAS", className="btn btn-neutral"),
                href="https://mytcas.com/", target="_blank"
            ),
            className="navbar-end"
        )
    ], className="navbar bg-base-200 shadow-sm"),

    # Main dashboard
    html.Div([
        html.Div([
            # Left: Map and Dropdown
            html.Div([
                html.H2("🌍 Universities Location Map", style={
                    "fontSize": "1.25rem", "fontWeight": "600", "marginBottom": "1rem", "textAlign": "center"
                }),
                dcc.Dropdown(
                    id='university-dropdown',
                    options=[
                        {'label': name, 'value': name}
                        for name in data_location['university_name_th'].unique()
                    ],
                    placeholder="🔍 เลือกมหาวิทยาลัย",
                    style={"marginBottom": "1rem"}
                ),
                dcc.Graph(
                    id="map-graph",
                    config={
                        "scrollZoom": True,
                        "displayModeBar": True,
                        "displaylogo": False
                    },
                    style={"width": "100%"}
                )
            ], style={
                "width": "50%", "height": "100vh",
                "background": "#fff",
                "boxShadow": "0 2px 8px #e5e7eb",
                "padding": "1.5rem"
            }),

            # Right: Bar charts
            html.Div([
                html.H2("📊 ค่าใช้จ่ายตลอดหลักสูตร", style={
                    "fontSize": "1.25rem", "fontWeight": "600", "marginBottom": "1rem"
                }),
                dcc.Graph(figure=create_bar_cost(data), style={"height": "45%"}),

                html.H2("📊 จำนวนหลักสูตรแต่ละสาขาในแต่ละมหาวิทยาลัย", style={
                    "fontSize": "1.25rem", "fontWeight": "600", "marginBottom": "1rem", "marginTop": "2rem"
                }),
                dcc.Graph(figure=create_bar_group(data), style={"height": "45%"})
            ], style={
                "height": "100vh", "width": "50%",
                "background": "#fff",
                "boxShadow": "0 2px 8px #e5e7eb",
                "padding": "1.5rem",
                "display": "flex", "flexDirection": "column", "justifyContent": "space-between"
            }),
        ], style={"display": "flex", "width": "100%"}),

        # Bottom: Optional content area
        html.Div([
            html.Div([
                html.H2("📊 University Acceptance Data", className="text-xl font-semibold mb-4"),
                dcc.Graph(figure=px.bar(data, x='info', y='cost'))
            ], className="card bg-base-100 shadow-xl p-6")
        ], className="w-full lg:w-1/2 p-4")
    ], className="flex flex-wrap justify-center")
], className="container mx-auto py-4")

# ===== Callback =====

@app.callback(
    Output('map-graph', 'figure'),
    Input('university-dropdown', 'value')
)
def update_map(selected_uni):
    return create_map_figure(selected_uni)

# ===== Run the app =====
if __name__ == '__main__':
    app.run(debug=True)
