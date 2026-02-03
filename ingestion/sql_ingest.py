import sqlite3
import os

os.makedirs("data/sql", exist_ok=True)
conn = sqlite3.connect("data/sql/assets.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS asset_usage (
    asset_id TEXT,
    date TEXT,
    energy_kwh REAL,
    status TEXT
)
""")

rows = [
    ("A1", "2024-01-01", 1200, "normal"),
    ("A1", "2024-02-01", 2500, "abnormal"),
    ("A2", "2024-02-01", 900, "normal"),
    ("A3", "2024-02-01", 3000, "abnormal"),
]

cur.executemany("INSERT INTO asset_usage VALUES (?,?,?,?)", rows)
conn.commit()
conn.close()
