# Import packages
from dash import Dash, html, dcc, Input, Output, dash_table
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np

# Load data
data_location = pd.read_csv("data/filtered_ai_com_courses.csv")
data = pd.read_excel("data/final_filtered_ai_com_courses.xlsx")

# Modern color palette
colors = {
    'primary': '#3B82F6',
    'secondary': '#8B5CF6',
    'accent': '#10B981',
    'warning': '#F59E0B',
    'error': '#EF4444',
    'background': '#F8FAFC',
    'surface': '#FFFFFF',
    'text': '#1E293B',
    'text_secondary': '#64748B'
}

# External stylesheets - Modern UI framework
external_stylesheets = [
    "https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css",
    "https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap"
]

# Initialize Dash app with custom styling
app = Dash(__name__, external_stylesheets=external_stylesheets)

# ===== Enhanced Helper Functions =====

def create_modern_bar_cost(data):
    """Create a modern cost analysis chart"""
    fig = px.bar(
        data, 
        x='info', 
        y='cost',
        color='cost',
        color_continuous_scale='viridis',
        title="ค่าใช้จ่ายตลอดหลักสูตร"
    )
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(family="Inter", size=12, color=colors['text']),
        title=dict(font=dict(size=18, color=colors['text'], family="Inter")),
        xaxis=dict(
            showticklabels=False,
            title="หลักสูตร",
            gridcolor='rgba(0,0,0,0.1)',
            title_font=dict(size=14, color=colors['text_secondary'])
        ),
        yaxis=dict(
            title="ราคา (บาท)",
            gridcolor='rgba(0,0,0,0.1)',
            title_font=dict(size=14, color=colors['text_secondary'])
        ),
        margin=dict(t=60, b=40, l=60, r=40),
        height=350
    )
    fig.update_traces(
        marker_line_width=0,
        hovertemplate='<b>ราคา:</b> %{y:,.0f} บาท<extra></extra>'
    )
    return fig

def create_modern_bar_group(data):
    """Create a modern grouped bar chart"""
    fig = px.histogram(
        data, 
        x="university_name_th", 
        color="field_name_en",
        barmode="group",
        title="จำนวนหลักสูตรในแต่ละมหาวิทยาลัย",
        color_discrete_sequence=px.colors.qualitative.Set3
    )
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(family="Inter", size=12, color=colors['text']),
        title=dict(font=dict(size=18, color=colors['text'], family="Inter")),
        xaxis=dict(
            showticklabels=False,
            title="มหาวิทยาลัย",
            gridcolor='rgba(0,0,0,0.1)',
            title_font=dict(size=14, color=colors['text_secondary'])
        ),
        yaxis=dict(
            title="จำนวนหลักสูตร",
            gridcolor='rgba(0,0,0,0.1)',
            title_font=dict(size=14, color=colors['text_secondary'])
        ),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="center",
            x=0.5,
            font=dict(size=11)
        ),
        margin=dict(t=80, b=40, l=60, r=40),
        height=350
    )
    return fig

def create_enhanced_map(selected_uni=None):
    """Create an enhanced interactive map"""
    df = data_location.copy()
    
    # Create custom markers based on university type or data
    marker_colors = ['#3B82F6', '#8B5CF6', '#10B981', '#F59E0B', '#EF4444']
    df['color'] = [marker_colors[i % len(marker_colors)] for i in range(len(df))]
    
    fig = go.Figure()
    
    # Add markers for all universities
    fig.add_trace(go.Scattermapbox(
        lat=df['latitude'],
        lon=df['longitude'],
        mode='markers',
        marker=dict(
            size=14,
            color=df['color'],
            opacity=0.8,
            sizemode='diameter'
        ),
        text=df['university_name_th'],
        hovertemplate='<b>%{text}</b><br>' +
                     'พิกัด: %{lat:.4f}, %{lon:.4f}<br>' +
                     '<extra></extra>',
        name="Universities"
    ))
    
    # Highlight selected university
    if selected_uni:
        selected = df[df['university_name_th'] == selected_uni]
        if not selected.empty:
            fig.add_trace(go.Scattermapbox(
                lat=[selected.iloc[0]['latitude']],
                lon=[selected.iloc[0]['longitude']],
                mode='markers',
                marker=dict(size=20, color='red', opacity=1),
                text=[selected_uni],
                hovertemplate='<b>%{text}</b> (เลือก)<br>' +
                             'พิกัด: %{lat:.4f}, %{lon:.4f}<br>' +
                             '<extra></extra>',
                name="Selected"
            ))
    
    # Set map center and zoom
    center_lat, center_lon, zoom = 13.7563, 100.5018, 6
    if selected_uni:
        selected = df[df['university_name_th'] == selected_uni]
        if not selected.empty:
            center_lat = selected.iloc[0]['latitude']
            center_lon = selected.iloc[0]['longitude']
            zoom = 10
    
    fig.update_layout(
        mapbox=dict(
            style="open-street-map",
            center=dict(lat=center_lat, lon=center_lon),
            zoom=zoom
        ),
        height=500,
        margin=dict(r=0, t=0, l=0, b=0),
        showlegend=False
    )
    
    return fig

def create_statistics_cards(data):
    """Create statistics summary cards"""
    total_courses = len(data)
    total_universities = data['university_name_th'].nunique()
    avg_cost = data['cost'].mean()
    min_cost = data['cost'].min()
    max_cost = data['cost'].max()
    
    return {
        'total_courses': total_courses,
        'total_universities': total_universities,
        'avg_cost': avg_cost,
        'min_cost': min_cost,
        'max_cost': max_cost
    }

# ===== Modern App Layout =====

# Get statistics
stats = create_statistics_cards(data)

app.layout = html.Div([
    # Modern Header
    html.Div([
        html.Div([
            html.Div([
                html.H1("🎓 TCAS68 Dashboard", 
                       className="text-3xl font-bold text-gray-800"),
                html.P("ระบบวิเคราะห์ข้อมูลหลักสูตรคอมพิวเตอร์และปัญญาประดิษฐ์", 
                       className="text-gray-600 mt-2")
            ], className="flex-1"),
            
            html.Div([
                html.A(
                    html.Button([
                        html.Span("🌐", className="mr-2"),
                        "เว็บไซต์ TCAS"
                    ], className="bg-blue-600 hover:bg-blue-700 text-white font-semibold py-2 px-6 rounded-lg transition-colors duration-200"),
                    href="https://mytcas.com/", 
                    target="_blank"
                )
            ])
        ], className="flex items-center justify-between")
    ], className="bg-white shadow-sm border-b px-6 py-4"),
    
    # Statistics Cards
    html.Div([
        html.Div([
            # Card 1: Total Courses
            html.Div([
                html.Div([
                    html.Div("📚", className="text-3xl mb-2"),
                    html.H3(f"{stats['total_courses']}", className="text-2xl font-bold text-gray-800"),
                    html.P("หลักสูตรทั้งหมด", className="text-gray-600 text-sm")
                ], className="text-center")
            ], className="bg-white rounded-xl shadow-lg p-6 border border-gray-100"),
            
            # Card 2: Universities
            html.Div([
                html.Div([
                    html.Div("🏛️", className="text-3xl mb-2"),
                    html.H3(f"{stats['total_universities']}", className="text-2xl font-bold text-gray-800"),
                    html.P("มหาวิทยาลัย", className="text-gray-600 text-sm")
                ], className="text-center")
            ], className="bg-white rounded-xl shadow-lg p-6 border border-gray-100"),
            
            # Card 3: Average Cost
            html.Div([
                html.Div([
                    html.Div("💰", className="text-3xl mb-2"),
                    html.H3(f"{stats['avg_cost']:,.0f}", className="text-2xl font-bold text-gray-800"),
                    html.P("ค่าใช้จ่ายเฉลี่ย (บาท)", className="text-gray-600 text-sm")
                ], className="text-center")
            ], className="bg-white rounded-xl shadow-lg p-6 border border-gray-100"),
            
            # Card 4: Cost Range
            html.Div([
                html.Div([
                    html.Div("📊", className="text-3xl mb-2"),
                    html.H3(f"{stats['min_cost']:,.0f} - {stats['max_cost']:,.0f}", className="text-xl font-bold text-gray-800"),
                    html.P("ช่วงค่าใช้จ่าย (บาท)", className="text-gray-600 text-sm")
                ], className="text-center")
            ], className="bg-white rounded-xl shadow-lg p-6 border border-gray-100"),
        ], className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8")
    ], className="px-6 py-6 bg-gray-50"),
    
    # Main Content Area
    html.Div([
        # Left Panel: Map
        html.Div([
            html.Div([
                html.Div([
                    html.H2("🗺️ แผนที่มหาวิทยาลัย", 
                           className="text-xl font-semibold text-gray-800 mb-4"),
                    
                    # Enhanced Dropdown
                    html.Div([
                        dcc.Dropdown(
                            id='university-dropdown',
                            options=[
                                {'label': f"📍 {name}", 'value': name}
                                for name in sorted(data_location['university_name_th'].unique())
                            ],
                            placeholder="🔍 เลือกมหาวิทยาลัยเพื่อดูตำแหน่ง",
                            className="mb-4",
                            style={
                                'fontFamily': 'Inter',
                                'fontSize': '14px'
                            }
                        )
                    ]),
                    
                    # Map
                    dcc.Graph(
                        id="map-graph",
                        config={
                            "scrollZoom": True,
                            "displayModeBar": True,
                            "displaylogo": False,
                            "modeBarButtonsToRemove": ['pan2d','lasso2d']
                        }
                    )
                ], className="bg-white rounded-xl shadow-lg p-6 border border-gray-100")
            ])
        ], className="w-full lg:w-1/2 pr-0 lg:pr-3"),
        
        # Right Panel: Charts
        html.Div([
            # Cost Chart
            html.Div([
                html.Div([
                    dcc.Graph(id="cost-chart")
                ], className="bg-white rounded-xl shadow-lg p-6 border border-gray-100 mb-6")
            ]),
            
            # University Programs Chart
            html.Div([
                html.Div([
                    dcc.Graph(id="programs-chart")
                ], className="bg-white rounded-xl shadow-lg p-6 border border-gray-100")
            ])
        ], className="w-full lg:w-1/2 pl-0 lg:pl-3")
    ], className="flex flex-col lg:flex-row px-6 pb-6"),
    
    # Footer
    html.Div([
        html.Div([
            html.P("© 2024 TCAS68 Dashboard | ข้อมูลจากระบบ TCAS", 
                   className="text-gray-600 text-center text-sm")
        ])
    ], className="bg-white border-t px-6 py-4 mt-8")
    
], className="min-h-screen bg-gray-50", style={'fontFamily': 'Inter'})

# ===== Enhanced Callbacks =====

@app.callback(
    [Output('map-graph', 'figure'),
     Output('cost-chart', 'figure'),
     Output('programs-chart', 'figure')],
    Input('university-dropdown', 'value')
)
def update_dashboard(selected_uni):
    # Update map
    map_fig = create_enhanced_map(selected_uni)
    
    # Update charts
    cost_fig = create_modern_bar_cost(data)
    programs_fig = create_modern_bar_group(data)
    
    return map_fig, cost_fig, programs_fig

# ===== Run the app =====
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8050)