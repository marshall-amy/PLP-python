import pandas as pd
import seaborn as sns
df=sns.load_dataset("iris")
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum)

print("Mean values:\n",df.mean(numeric_only=True))
print("Median values:\n",df.median(numeric_only=True))
print("Standard deviation:\n",df.std(numeric_only=True))
grouped=df.groupby("species").mean()
print(grouped)

import matplotlib.pyplot as plt
df["sepal_length"].plot(kind="line",title="Sepal Length Trend")
plt.xlabel("index")
plt.ylabel("Sepal Length")
plt.show()
df.groupby("species")["petal_length"].mean().plot(kind="bar",title="Average Petal Length by Species")
plt.ylabel("Petal Length")
plt.show()
df["sepal_width"].plot(kind="hist",bins=10,title="Sepal Width Distribution")
plt.xlabel("Sepal Width")
plt.show()
df.plot(kind="scatter",x="srepal_length",y="petal_length",title="Sepal Length vs Petal Length")
plt.show()