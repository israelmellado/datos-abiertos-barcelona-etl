import pandas as pd
import requests

url = "PEGA_AQUI_LA_API_REAL"

response = requests.get(url)

data = response.json()

df = pd.DataFrame(data)

print(df.head())

df.to_csv("../datos/crudos/obras.csv", index=False)
