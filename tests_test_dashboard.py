import pytest
from dashboard.charts import display_charts
import pandas as pd
import os

@pytest.fixture
def test_file(tmp_path):
    file_path = tmp_path / "test_statistics.csv"
    data = {
        'TEAM': ['Team A', 'Team B'],
        'matches_played': [10, 12],
        'win_rate': [50, 60],
        'goal_difference': [5, 10],
    }
    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False)
    return file_path

def test_display_charts(test_file):
    assert os.path.exists(test_file)
    # Assuming display_charts writes some output, we can test side-effects
    # For now, just ensure no exceptions occur
    display_charts(test_file)