import requests
import json

DATASET = "obres"

url = (
    "https://opendata-ajuntament.barcelona.cat/data/api/3/action/"
    f"package_show?id={DATASET}"
)

response = requests.get(url)

print(f"Código HTTP: {response.status_code}")

if response.status_code == 200:
    data = response.json()

    if data["success"]:
        print("\nNombre del dataset:")
        print(data["result"]["title"])

        print("\nRecursos disponibles:\n")

        for recurso in data["result"]["resources"]:
            print("-" * 60)
            print("Nombre :", recurso.get("name"))
            print("Formato:", recurso.get("format"))
            print("ID     :", recurso.get("id"))
            print("URL    :", recurso.get("url"))
    else:
        print("La API respondió, pero indicó un error.")
else:
    print("Error al acceder a la API.")