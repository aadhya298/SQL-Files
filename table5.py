import sqlite3
import pandas as pd

conn= sqlite3.connect("d1.db")
print("Connection established")

conn.execute(""" 
    CREATE TABLE IF NOT EXISTS STUDENTS(
        STUDENT_ID INTEGER PRIMARY KEY,
        NAME TEXT,
        CLASS INTEGER,
        CITY TEXT
        );
""")
conn.execute(""" 
    CREATE TABLE IF NOT EXISTS MARKS(
        STUDENT_ID PRIMARY KEY,
        SUBJECT TEXT,
        MARKS REAL
        );
""")
conn.execute("""INSERT OR IGNORE INTO Students (student_id, name, class, city) VALUES
(1, 'Aadhya', 11, 'Delhi'),
(2, 'Rohan', 12, 'Mumbai'),
(3, 'Sneha', 11, 'Pune'),
(4, 'Arjun', 12, 'Chennai'),
(5, 'Kavya', 11, 'Delhi');""")
conn.execute("""INSERT OR IGNORE INTO Marks (student_id, subject, marks) VALUES
(1, 'Physics', 85),
(1, 'Maths', 92),
(2, 'Physics', 78),
(3, 'Maths', 88),
(4, 'Chemistry', 90),
(6, 'Physics', 70);""")
conn.commit()

df_1= pd.read_sql("SELECT * FROM STUDENTS", conn)
df_2= pd.read_sql("SELECT * FROM MARKS", conn)
print(df_1)
print(df_2)
a=pd.read_sql("SELECT S.NAME, M.SUBJECT, M.MARKS FROM STUDENTS AS S JOIN MARKS AS M ON S.STUDENT_ID==M.STUDENT_ID ORDER BY M.MARKS DESC", conn)
print(a)
b=pd.read_sql("SELECT S.NAME, M.SUBJECT, M.MARKS FROM STUDENTS AS S LEFT JOIN MARKS AS M ON S.STUDENT_ID==M.STUDENT_ID ORDER BY M.MARKS DESC", conn)
print(b)
c=pd.read_sql("SELECT S.NAME, M.SUBJECT, M.MARKS FROM STUDENTS AS S RIGHT JOIN MARKS AS M ON S.STUDENT_ID==M.STUDENT_ID ORDER BY M.MARKS DESC", conn)
print(c)
d=pd.read_sql("SELECT S.NAME, M.SUBJECT, M.MARKS FROM STUDENTS AS S CROSS JOIN MARKS AS M ON S.STUDENT_ID==M.STUDENT_ID ORDER BY M.MARKS DESC", conn)
print(d)
p=pd.read_sql("SELECT NAME FROM STUDENTS UNION SELECT SUBJECT FROM MARKS",conn)
print(p)