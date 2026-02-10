import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df= pd.read_csv("Weather.csv")
print(df.head(5))
print(df.info())

#Bar plot
sns.barplot(x=df['humidity'], y=df['temperature'])
plt.show()

# Displot
sns.displot(df['humidity'], kde=False)
plt.show()

sns.displot(df['humidity'], kde=True)
plt.show()

#Joint plot
sns.jointplot(x=df['humidity'], y=df['temperature'])
plt.show()

sns.jointplot(x=df['humidity'], y=df['temperature'], kind='hex')
plt.show()

sns.jointplot(x=df['humidity'], y=df['temperature'], kind='kde')
plt.show()

#Pair plot
sns.pairplot(df[['humidity','temperature','air_pollution_index']])
plt.show()

#Strip plot
sns.stripplot(x=df['weather_type'], y=df['temperature'])
plt.show()

#Swarm plot
sns.swarmplot(x=df['humidity'], y=df['temperature'])
plt.show()

#Count Plot
sns.countplot(x=df['weather_type'])
plt.show()

# Point plot
sns.pointplot(x=df['humidity'], y=df['temperature'])
plt.show()