import pandas as pd
from pathlib import Path
from .db_utils import get_engine, write_df

CLEAN_DATA_DIR = Path('data/cleaned')

# Export clean dataframes to csv
def export_dfs(dataframes: dict[str, pd.DataFrame], path: str, file_format: str, index: bool) -> None:
    for name, df in dataframes.items():
        if file_format == '.csv':
            df.to_csv(Path(path) / f'{name}_data_cleaned.csv', index=index)
        else:
            raise ValueError('Unsupported file format: must use .csv')
        
    
# Write data to database
def load_to_postgres(tables: dict[str, pd.DataFrame]) -> None:
    engine = get_engine()

    for table, df in tables.items():
        write_df(df, table, engine, if_exists='append')
