

import json
import os

def cargar_json(ruta):
   
    if not os.path.exists(ruta):
        return []
    
    
    with open(ruta, "r") as archivo:
        return json.load(archivo)

def guardar_json(ruta, datos):
   
    with open(ruta, "w") as archivo:
        json.dump(datos, archivo, indent=4)



