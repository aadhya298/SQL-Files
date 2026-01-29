import pandas as pd
import numpy as np

exam_data={"Name":['Rudraksh','Aalok','Aadhya','Sagar','Anamika','Avni','Ayush','Nishant','Harshit','Akshat'],
           "Score":[21,13,18,np.nan,12,9,17,np.nan,16,20],
           "Attempts":[2,3,1,4,3,2,1,3,2,2],
           "Qualify":['Yes','No','Yes','Yes','Yes','No','No','No','Yes','Yes']
           }
i=['a','b','c','d','e','f','g','h','i','j']
df= pd.DataFrame(exam_data, index=i)
print(df)
print(df.head(4))
print(df.tail(3))
print(df.info())
print(df.describe())
print(df.columns)
print(df.isnull().sum())
print(df.isnull().any())