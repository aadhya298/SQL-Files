import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

df= pd.read_csv('USA_Housing.csv')

print(df.head(10))
print(df.info())
print(df.describe())
print(df.columns)

sns.pairplot(df)

numeric_df = df.select_dtypes(include=np.number)

sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm")

plt.show()