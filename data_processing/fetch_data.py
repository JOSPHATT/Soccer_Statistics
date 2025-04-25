import pandas as pd

def fetch_data(data_url):
    try:
        # Fetch and load the data
        df = pd.read_csv(data_url)
        return df
    except Exception as e:
        print(f"Error fetching or reading data from the URL: {e}")
        raise e
