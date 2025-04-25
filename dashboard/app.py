import streamlit as st
from dashboard.charts import display_charts
from utils.file_operations import save_to_csv
from data_processing.fetch_data import fetch_data
from data_processing.process_statistics import preprocess_data, process_team_statistics

DATA_URL = 'https://raw.githubusercontent.com/JOSPHATT/Finished_Matches/refs/heads/main/Finished_matches.csv'
CSV_FILE_PATH = 'team_statistics.csv'

def main():
    # Fetch and process data
    try:
        df = fetch_data(DATA_URL)
        df = preprocess_data(df)
        team_stats = process_team_statistics(df)
        save_to_csv(team_stats, CSV_FILE_PATH)
    except Exception as e:
        st.error(f"Error processing team statistics: {e}")
        return

    # Display dashboard
    display_charts(CSV_FILE_PATH)

if __name__ == "__main__":
    main()
