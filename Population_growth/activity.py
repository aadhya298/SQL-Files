import pandas as pd
import matplotlib.pyplot as plt

df= pd.read_csv('Population_growth\countries.csv')
df.head(10)

# Extract the rows where year is 1952 and 2007
d_52= df.loc[df['year'] == 1952]
d_07= df.loc[df['year'] == 2007]
d_52.head()
d_07.head()

type(d_52)

# Merge 1952 and 2007 dataframes together
merge= d_52.merge(d_07, left_on='country',right_on='country')
merge.head()

# Drop both year columns
merge.drop(['year_x' , 'year_y'], axis=1)
merge.head()

#Create a new column that takes the difference b/w population_y and population_x column
merge['population_growth']= merge['population_y']-merge['population_x']
merge.head()

#Test the math
31889923 - 8425333

merge.shape, type(merge)

#Sort the values so you get back the 10 countries with the biggest population growth
merge= merge.sort_values('population_growth' , ascending=False).head(10)
merge.head(10)

#Lets plot the data
names=['China','India','United States','Indonesia','Brazil','Pakistan','Bangladesh','Nigeria','Mexico','Philippines']
pop_grow= (merge['population_growth']/10**6)

plt.figure(figsize=(15,9))
plt.bar(names,pop_grow,width=0.6)
plt.xlabel('Country')
plt.ylabel('Population Growth (Millions)')
plt.title("Top 10 Countries w/the Biggest Population Growth From 1952 To 2007")
plt.xticks(rotation=45)

#zip joins x and y coordinates in pairs
for x,y in zip(names,pop_grow):
    label = "({:,2f}", format(y)

    plt.annotate(label, #text
                 (x,y), # point to label
                 textcoords='offset points', #position of text
                 xytext=(0,10), #distance b/w text and (x,y)
                 ha='center') #horizontal alignment(left/right/center) 

plt.show()