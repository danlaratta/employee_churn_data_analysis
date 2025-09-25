from sqlalchemy import create_engine
from . import config 
import pandas as pd
from typing import Literal


# Create and return engine
def get_engine(echo: bool = False):
    return create_engine(config.DB_URL, echo=echo)


# Load clean dataframes into DB
def write_df(df: pd.DataFrame, table_name: str, engine, if_exists: Literal['fail', 'append'] = 'append') -> None:
    df.to_sql(name= table_name, con=engine, index=False, if_exists=if_exists) # convert df into sql table and load into postgres