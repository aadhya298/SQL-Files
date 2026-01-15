import sqlite3
import pandas as pd

conn= sqlite3.connect("d1.db")
print("Connection established successfully")

conn.execute(""" 
CREATE TABLE IF NOT EXISTS Match (
    Match_Id INTEGER PRIMARY KEY,
    Season_Id INTEGER,
    Match_Winner TEXT NOT NULL,
    Win_Margin INTEGER,
    Venue_Id INTEGER NOT NULL
    )
""")

conn.execute("INSERT OR IGNORE INTO MATCH VALUES(1,NULL,'MI',45,101)")
conn.execute("INSERT OR IGNORE INTO MATCH VALUES(2,9,'CSK',50,102)")
conn.execute("INSERT OR IGNORE INTO MATCH VALUES(3,NULL,'RCB',8,103)")
conn.execute("INSERT OR IGNORE INTO MATCH VALUES(4,8,'MI',30,101)")
conn.execute("INSERT OR IGNORE INTO MATCH VALUES(5,'','KKR',22,104)")
conn.commit()

df= pd.read_sql("SELECT * FROM MATCH", conn)
print(df)
a= pd.read_sql("SELECT * FROM MATCH WHERE SEASON_ID='' ", conn)
print(a)
b= pd.read_sql("SELECT * FROM MATCH WHERE SEASON_ID=NULL", conn)
print(b)