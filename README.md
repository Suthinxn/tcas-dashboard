# TCAS Dashboard
![dashboard](https://github.com/Suthinxn/tcas-dashboard/blob/main/dashboard-demo.png)
This project is part of the course  **241-353 ART INTELL ECOSYSTEM MODULE**

A web-based dashboard application for TCAS (Thai University Central Admission System) data visualization and analysis. This project includes data scraping, cleaning, geocoding, and interactive dashboard features for Computer Engineering, Artificial Intelligence Engineering.

create by : 6610110341 สุธินันท์ รองพล

## Features

-   **Data Scraping**: Automated data collection from TCAS API
-   **Data Cleaning**: Process and filter Computer Engineering and Artificial Intelligence Engineering course data
-   **Geocoding**: Get geographical coordinates for universities
-   **Interactive Dashboard**: Web-based visualization and analysis tools

## Prerequisites

-   Python 3.8 or higher
-   Poetry (Python dependency management tool)
-   Jupyter Notebook (for data cleaning operations)

## Installation

### 1. Clone the Repository

Choose either HTTPS or SSH method:

**HTTPS:**

```bash
git clone https://github.com/Suthinxn/tcas-dashboard.git

```

**SSH:**

```bash
git clone git@github.com:Suthinxn/tcas-dashboard.git

```

### 2. Navigate to Project Directory

```bash
cd tcas-dashboard

```

### 3. Install Dependencies

```bash
poetry install

```

### 4. Activate Virtual Environment

```bash
poetry shell

```

## Running the Application

### 1. Navigate to App Directory

```bash
cd app

```

### 2. Start the Server

```bash
python main.py

```

### 3. Access the Application

Open your web browser and navigate to:

```
http://localhost:8050/

```

## Project Structure

```
tcas-dashboard/
├── app/
│   ├── data/
│   │   ├── filtered_ai_com_courses.csv      # Processed course data (CSV)
│   │   └── final_filtered_ai_com_courses.xlsx # Processed course data (Excel)
│   │
│   ├── clean_ai_com_courses.ipynb           # Data cleaning notebook
│   ├── geocode_universities.py              # Get geolocation data
│   ├── main.py                              # Main application file
│   └── scraping.py                          # Get data from API
│
├── pyproject.toml                           # Poetry configuration
└── README.md                               # This file

```

## Data Pipeline

The project follows this data processing workflow:

1.  **Data Scraping** (`scraping.py`): Collect raw data from TCAS API
2.  **Data Cleaning** (`clean_ai_com_courses.ipynb`): Process and filter the data
3.  **Geocoding** (`geocode_universities.py`): Add location coordinates
4.  **Dashboard** (`main.py`): Visualize the processed data

## Development

If you're using an IDE, make sure to select the Python interpreter from the `tcas-dashboard` virtual environment created by Poetry.

## Troubleshooting

-   **Port already in use**: If port 8050 is already in use, the application will automatically try to use another available port
-   **Dependencies issues**: Run `poetry install` again to ensure all dependencies are properly installed
-   **Python version**: Make sure you're using Python 3.8 or higher

## Contributing

1.  Fork the repository
2.  Create a feature branch
3.  Make your changes
4.  Submit a pull request

