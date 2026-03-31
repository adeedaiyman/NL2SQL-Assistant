import sqlite3

# Connect to database (this will create file automatically)
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE sales (
    order_id INTEGER,
    customer_name TEXT,
    product TEXT,
    region TEXT,
    revenue REAL,
    order_date TEXT
)
""")

conn.commit()
conn.close()

print("Database and table created successfully!")