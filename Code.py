import requests
import pandas as pd
import io

url = "https://ckan0.cf.opendata.inter.prod-toronto.ca/dataset/b68cb71b-44a7-4394-97e2-5d2f41462a5d/resource/ecc4f0a8-25e6-40d8-ae70-8006e38c4f9a/download/ttc-streetcar-delay-data-2021.xlsx"

s = requests.get(url).content
df = pd.read_excel(io.BytesIO(s))
df.to_csv('ttc-streetcar-delay-data-2021.csv', index=False)

df = pd.read_csv('ttc-streetcar-delay-data-2021.csv')
df.head(3)

print('shape:', df.shape, '\n', 'describe:', df.describe(), '\n', 'info:', df.info(), '\n', 'values:', df.values, '\n', 'columns:', df.columns, sep='\n')

# EDA. The folliwng is a list of 5 exploratory data analysis (EDA) questions.
# 1. What is the distribution of the delay time?
# 2. What is the relationship between delay time and the number of passengers?

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10,6))
sns.distplot(df['Min Delay'], bins=50)
plt.show()

df['Day'] = df['Date'].dt.day_name()

plt.figure(figsize=(10,6))
sns.boxplot(x=df.dt.Time , y='Min Delay', data=df)
plt.show()