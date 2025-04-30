# Scraper Project

This Python project is designed to scrape statistics about popular movies (Latest International Weekends) from the website **https://www.boxofficemojo.com/** and analyze the collected information.

## Features Overview

### 1. Scraping Movies Data
   - **Script**: `src/scraper/main.py`
   - **Description**: This script scrapes movie data from **https://www.boxofficemojo.com/**, including titles, ratings, genres, and release dates, and saves the extracted information into a structured format.
   - **Output**: CSV file containing movie data.
   - **Example usage**:
     ```sh
     python src/scraper/main.py
     ```

### 2. Data Analysis
   - **Script**: `src/analysis/cli.py <file_path>` 
   - **Description**: Analyzes the collected movie data, generating insights such as trends and statistics and making corresponding charts. 
   - **Collected movies data and analysis results**: https://drive.google.com/drive/folders/1XjMVG4IoDzCp7jmNPmM97u6RqfXHp_sb?usp=sharingV
   - **Output**: Excel reports and PNG visualizations.
   - **Example usage**:
     ```sh
     python src/analysis/cli.py data/movies.csv
     ```

### 3. Workflow Automation
   - **Script**: `airflow/dags/flow.py`
   - **Description**: Defines an Airflow DAG to automate the scraping process on a scheduled basis.
   - **Functionality**:
     - Runs the scraper to collect new data.
     - Parses and stores the collected data.
     - Runs on schedule in Windows Task Planner.
   - **Usage**:
     - To enable automated execution, integrate the DAG into an Airflow instance.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/nativa23/scraper-project.git
    ```
2. Navigate to the project folder:
    ```sh
    cd scraper-project
    ```
3. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```
## License
This project is open and available for use without any restrictions. You are free to use, modify, and distribute the code.

