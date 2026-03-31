import pandas as pd
import sqlite3

data = {
    "order_id": [1,2,3,4,5,6,7,8],
    "customer_name": ["Aman","Ali","John","Sara","Riya","David","Priya","Rahul"],
    "product": ["Laptop","Phone","Tablet","Laptop","Phone","Tablet","Laptop","Phone"],
    "region": ["North","South","East","West","North","East","South","West"],
    "revenue": [50000,20000,15000,60000,25000,18000,70000,22000],
    "order_date": [
        "2024-01-01","2024-01-02","2024-01-03","2024-01-04",
        "2024-01-05","2024-01-06","2024-01-07","2024-01-08"
    ]
}

df = pd.DataFrame(data)

conn = sqlite3.connect("database.db")
df.to_sql("sales", conn, if_exists="append", index=False)
conn.close()

print("Data inserted successfully!")