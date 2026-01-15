import sqlite3
import pandas as pd

conn= sqlite3.connect("d.db")
print("Connection established")


conn.execute("""
    CREATE TABLE IF NOT EXISTS CLASS(
        ROLL_NO INTEGER PRIMARY KEY,
        NAME TEXT NOT NULL,
        CLASS INTEGER DEFAULT(11),
        EMAIL_ID TEXT UNIQUE    
    )   
""")

conn.execute("INSERT OR IGNORE INTO CLASS(ROLL_NO,NAME,EMAIL_ID) VALUES(1,'AADHYA','aadhya.11@yahoo.com')")
conn.execute("INSERT OR IGNORE INTO CLASS(ROLL_NO,NAME,EMAIL_ID) VALUES(2,'ANAMIKA','anamika.22@rediff.com')")
conn.execute("INSERT OR IGNORE INTO CLASS(ROLL_NO,NAME,EMAIL_ID) VALUES(3,'AVNI','avni.41@yahoo.com')")
conn.execute("INSERT OR IGNORE INTO CLASS(ROLL_NO,NAME,EMAIL_ID) VALUES(4,'SAGAR','sagar.08@rediff.com')")
conn.commit()

df= pd.read_sql("SELECT * FROM CLASS", conn)
print(df)