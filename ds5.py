import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

df= pd.read_csv("USA_Housing.csv")

print(df.head(8))
print(df.info())
print(df.describe())
print(df.columns)

sns.pairplot(df)
num_df= df.select_dtypes(include=np.number)
sns.heatmap(num_df.corr(), annot=True)
plt.show()