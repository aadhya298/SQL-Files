-- Create a table SALESMAN with columns Salesman_id , Name, City, Comission
CREATE TABLE IF NOT EXISTS SALESMAN(
    SALESMAN_ID INTEGER PRIMARY KEY,
    NAME TEXT,
    CITY TEXT,
    COMISSION REAL
);
-- Create a table CUSTOMERS with columns Customer_id, Customer_name, City, Grade, Salesman_id
CREATE TABLE IF NOT EXISTS CUSTOMERS(
    CUSTOMER_ID INTEGER PRIMARY KEY,
    CUSTOMER_NAME TEXT,
    CITY TEXT,
    GRADE TEXT,
    SALESMAN_ID INTEGER
);
-- Create a table ORDERS with columns Order_no , Purchase_amt, Order_date, Customer_id, Salesman_id 
CREATE TABLE IF NOT EXISTS ORDERS(
    ORDER_NO INTEGER PRIMARY KEY,
    PURCHASE_AMT REAL,
    ORDER_DATE TEXT,
    CUSTOMER_ID INTEGER,
    SALESMAN_ID INTEGER
);
--Insertion of Data
INSERT INTO SALESMAN(SALESMAN_ID,NAME,CITY,COMISSION)VALUES
    (1,'Varun','Rishikesh',40.2),
    (2,'Aalok','Dehradun',30.6),
    (3,'Arjun','Rishikesh',75.8),
    (4,'Rudra','Delhi',80.0),
    (5,'Sagar','Rishikesh',12.5),
    (6,'Harsh','Dehradun',67.7),
    (7,'Abhimanyu','Delhi',91.0),
    (8,'Shyam','Rishikesh',53.5),
    (9,'Ritik','Delhi',71.1),
    (10,'Saurav','Dehradun',64.3);

INSERT INTO CUSTOMERS(CUSTOMER_ID,CUSTOMER_NAME,CITY,GRADE,SALESMAN_ID)VALUES
    (1,'Anamika','Rishikesh',350,5),
    (2,'Neil','Dehradun',150,8),
    (3,'Aadhya','Rishikesh',300,3),
    (4,'Aryan','Delhi',190,10),
    (5,'Avni','Rishikesh',230,7),
    (6,'Abhay','Dehradun',400,9),
    (7,'Aarush','Delhi',200,1),
    (8,'Anu','Rishikesh',50,2),
    (9,'Ritik','Delhi',250,4),
    (10,'Saurav','Dehradun',440,3);

INSERT INTO ORDERS(ORDER_NO,PURCHASE_AMT,ORDER_DATE,CUSTOMER_ID,SALESMAN_ID)VALUES
    (1,121.67,'2012-10-05',1,9),
    (2,183.67,'2012-11-20',1,9),
    (3,212.67,'2012-09-05',1,9),
    (4,562.67,'2012-12-05',1,9),
    (5,340.67,'2012-09-05',1,9),
    (6,361.37,'2012-02-05',1,9),
    (7,348.98,'2012-07-05',1,9),
    (8,879.12,'2012-08-05',1,9),
    (9,267.83,'2012-03-05',1,9),
    (10,222.22,'2012-1-40',1,9);

-- Select Customer_name Salesma_name, City 
SELECT CUSTOMERS.CUSTOMER_NAME,SALESMAN.NAME,SALESMAN.CITY FROM CUSTOMERS
JOIN SALESMAN ON CUSTOMERS.CITY=SALESMAN.CITY;