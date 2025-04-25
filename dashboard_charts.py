import streamlit as st
import pandas as pd
import plotly.express as px
import os

def display_charts(file_path):
    if not os.path.exists(file_path):
        st.error(f"The file {file_path} does not exist.")
        return

    try:
        data = pd.read_csv(file_path)
        # Display filtered data and charts
        st.title("Team Statistics Dashboard")
        st.dataframe(data)

        # Plot example: Win Rate Bar Chart
        fig = px.bar(data, x='TEAM', y='win_rate', title="Win Rate by Team", color='TEAM')
        st.plotly_chart(fig)
    except Exception as e:
        st.error(f"Error loading or visualizing data: {e}")