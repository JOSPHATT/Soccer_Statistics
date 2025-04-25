import pytest
import pandas as pd
from data_processing.fetch_data import fetch_data
from data_processing.process_statistics import preprocess_data, process_team_statistics

TEST_DATA_URL = 'https://raw.githubusercontent.com/JOSPHATT/Finished_Matches/refs/heads/main/Finished_matches.csv'

@pytest.fixture
def sample_data():
    return pd.DataFrame({
        'HOME': ['Team A', 'Team B'],
        'AWAY': ['Team C', 'Team D'],
        'H_GOALS': [2, 1],
        'A_GOALS': [1, 1],
    })

def test_fetch_data():
    df = fetch_data(TEST_DATA_URL)
    assert isinstance(df, pd.DataFrame)
    assert not df.empty

def test_preprocess_data(sample_data):
    preprocessed = preprocess_data(sample_data)
    assert 'home_team_goal' in preprocessed.columns
    assert 'away_team_goal' in preprocessed.columns
    assert preprocessed.isnull().sum().sum() == 0

def test_process_team_statistics(sample_data):
    preprocessed = preprocess_data(sample_data)
    team_stats = process_team_statistics(preprocessed)
    assert 'TEAM' in team_stats.columns
    assert 'win_rate' in team_stats.columns
