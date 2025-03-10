import mysql.connector
import pandas as pd
from config import DB_CONFIG

def execute_query(query):
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    
    cursor.execute(query)
    data = cursor.fetchall()
    
    df = pd.DataFrame(data, columns=[desc[0] for desc in cursor.description])
    
    cursor.close()
    conn.close()
    
    return df
