import os
import pandas as pd

def save_to_csv(df, file_path):
    try:
        if os.path.exists(file_path):
            # Append to the existing CSV file
            existing_data = pd.read_csv(file_path)
            combined_data = pd.concat([existing_data, df]).drop_duplicates().reset_index(drop=True)
            combined_data.to_csv(file_path, index=False)
        else:
            # Create the file if it doesn't exist
            df.to_csv(file_path, index=False)
    except Exception as e:
        print(f"Error during file writing: {e}")
        raise e