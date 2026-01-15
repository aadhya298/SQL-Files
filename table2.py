import sqlite3
import pandas as pd

conn= sqlite3.connect("datbase.db")
print("Connection established successfully")

conn.execute(""" 
CREATE TABLE IF NOT EXISTS Match (
    Match_Id INTEGER PRIMARY KEY,
    Season_Id INTEGER,
    Match_Winner TEXT,
    Win_Margin INTEGER,
    Venue_Id INTEGER
    )
""")

conn.execute("INSERT OR IGNORE INTO MATCH VALUES(1,2,'MI',45,101)")
conn.execute("INSERT OR IGNORE INTO MATCH VALUES(2,9,'CSK',50,102)")
conn.execute("INSERT OR IGNORE INTO MATCH VALUES(3,9,'RCB',8,103)")
conn.execute("INSERT OR IGNORE INTO MATCH VALUES(4,9,'MI',30,101)")
conn.execute("INSERT OR IGNORE INTO MATCH VALUES(5,9,'KKR',22,104)")
conn.commit()

df=pd.read_sql("SELECT * FROM MATCH", conn)
print(df)
# Select avg win margin from all the winning teams of season 9
a=pd.read_sql("SELECT MATCH_WINNER, AVG(WIN_MARGIN) FROM MATCH WHERE SEASON_ID=9 GROUP BY MATCH_WINNER ORDER BY AVG(WIN_MARGIN)  ", conn)
print(a)
# Count of all the venues of season 9
b= pd.read_sql("SELECT COUNT(DISTINCT(VENUE_ID)) FROM MATCH WHERE SEASON_ID=9", conn)
print(b)
# Find min max and avg of win margin
c= pd.read_sql("SELECT MIN(WIN_MARGIN), MAX(WIN_MARGIN), AVG(WIN_MARGIN) FROM MATCH", conn)
print(c)
# Find the sum of win margin of each team in the descending order of match_id
d= pd.read_sql("SELECT MATCH_WINNER, SUM(WIN_MARGIN) FROM MATCH GROUP BY MATCH_WINNER ORDER BY MATCH_ID DESC", conn)
print(d)
# Return the total no of win margins of all the winners
z= pd.read_sql("SELECT SUM(WIN_MARGIN) FROM MATCH WHERE SEASON_ID=9", conn) 
print(z)

conn.close()