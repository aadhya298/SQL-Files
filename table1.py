import sqlite3
import pandas as pd

conn= sqlite3.connect('data.db')

conn.execute("""
CREATE TABLE IF NOT EXISTS Player_Match (
    match_id INTEGER,
    player_id INTEGER,
    runs INTEGER,
    fours INTEGER,
    PRIMARY KEY (match_id, player_id)
)
""")

conn.execute("INSERT OR IGNORE INTO Player_Match VALUES (1, 101, 45, 4)")
conn.execute("INSERT OR IGNORE INTO Player_Match VALUES (1, 102, 30, 2)")
conn.execute("INSERT OR IGNORE INTO Player_Match VALUES (2, 101, 60, 6)")
conn.execute("INSERT OR IGNORE INTO Player_Match VALUES (2, 103, 25, 1)")

conn.commit()

df=pd.read_sql("SELECT * FROM PLAYER_MATCH", conn)
a= pd.read_sql("SELECT MATCH_ID, PLAYER_ID FROM PLAYER_MATCH", conn)
b= pd.read_sql("SELECT * FROM PLAYER_MATCH WHERE MATCH_ID=1", conn)
c= pd.read_sql("SELECT * FROM PLAYER_MATCH WHERE MATCH_ID IN (1,2)", conn)
d= pd.read_sql("SELECT * FROM PLAYER_MATCH WHERE PLAYER_ID LIKE '%101%' ", conn)
x= pd.read_sql("SELECT MIN(MATCH_ID), MAX(PLAYER_ID) FROM PLAYER_MATCH", conn)

df.info()
print(df)
print(a)
print(b)
print(c)
print(d)
print(x)
conn.close()