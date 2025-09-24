import pandas as pd
from pathlib import Path

# Path to store data
RAW_DIR = Path('data/raw')

# Get raw employee data
def get_raw_data():
    return pd.read_csv(RAW_DIR / 'employee_data.csv')
