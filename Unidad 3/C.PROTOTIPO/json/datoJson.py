import json

# Creación de un archivo JSON
data = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Buenos Aires"
}
with open('datos.json', 'w') as file:
    json.dump(data, file)

# Lectura de un archivo JSON
with open('datos.json', 'r') as file:
    data = json.load(file)
print(data)

# Modificación de un archivo JSON
data["edad"] = 31
with open('datos.json', 'w') as file:
    json.dump(data, file)

# Verificamos la modificación
with open('datos.json', 'r') as file:
    data = json.load(file)
print(data)


