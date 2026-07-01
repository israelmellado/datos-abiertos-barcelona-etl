import requests

url = "https://opendata-ajuntament.barcelona.cat/data/api/3/action/package_search?q=obres"

response = requests.get(url)

data = response.json()

for result in data["result"]["results"]:
    print(result["title"])
    print(result["name"])
    print("-" * 50)
  
input("\nPulsa Enter para salir...")