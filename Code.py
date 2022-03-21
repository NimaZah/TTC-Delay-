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

