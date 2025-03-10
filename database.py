from sqlalchemy import create_engine, text
import pandas as pd
from config import DB_CONFIG

engine = create_engine(DB_CONFIG['database_url'])

def execute_query(query):
    with engine.connect() as connection:
        result = connection.execute(text(query))
        data = result.fetchall()
        df = pd.DataFrame(data, columns=result.keys())
    return df
