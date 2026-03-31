import sqlite3
import pandas as pd

def run_query(query):
    # Safety check
    if "DROP" in query or "DELETE" in query:
        raise Exception("Unsafe query detected!")

    conn = sqlite3.connect("database.db")

    try:
        df = pd.read_sql_query(query, conn)
    except Exception as e:
        conn.close()
        raise e

    conn.close()
    return df