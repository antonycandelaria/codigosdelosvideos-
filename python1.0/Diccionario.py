number ={1: "uno",2:"dos",3:"tres"}
print(number[2])
informacion = {"nombre": "antony",
               "apellido":"candelaria",
               "altura": 1.60,
               "edad": 22}
print(informacion)
del informacion["edad"]
print(informacion)
claves = informacion.keys()
print(claves)
#print(type(claves))
values = informacion.values()
print(values)
pairs = informacion.items()
print(pairs)
contacts = {"antony": {"Apellido": "candelaria",
               "Altura": 1.60,
               "Edad": 22},
                "Diego": {"Apellido": "Antezana",
               "Altura": 1.80,
               "Edad": 32}}
print(contacts["antony"])