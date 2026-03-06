

from gestionarjson import cargar_json, guardar_json

RUTA = "herramientas.json"

def generar_id(lista):
    return 1 if not lista else lista[-1]["id"] + 1

def agregar_herramienta():
    herramientas = cargar_json(RUTA)

    nueva = {
        "id": generar_id(herramientas),
        "nombre": input("Nombre: "),
        "categoria": input("Categoría: "),
        "cantidad": int(input("Cantidad disponible: ")),
        "estado": "activa",
        "valor": float(input("Valor estimado: "))
    }

    herramientas.append(nueva)
    guardar_json(RUTA, herramientas)
    print("Herramienta agregada.")

def listar_herramientas():
    herramientas = cargar_json(RUTA)
    print("\n--- LISTA DE HERRAMIENTAS ---")
    
    print("ID\tNOMBRE\t\tCANT\tESTADO\tVALOR")

    print("-" * 40)
    
    for h in herramientas:
        
        print(f"{h['id']}\t{h['nombre']}\t\t{h['cantidad']}\t{h['estado']}\t${h['valor']}")

def buscar_herramienta():
    herramientas = cargar_json(RUTA)
    id_buscar = int(input("ID herramienta: "))
    for h in herramientas:
        if h["id"] == id_buscar:
            print(h)
            return h
    print("No encontrada.")

def actualizar_herramienta():
    herramientas = cargar_json(RUTA)
    id_buscar = int(input("ID herramienta a actualizar: "))
    for elemento in herramientas:
        if elemento["id"] == id_buscar:
            
            print(f"\nmodificando: {elemento['nombre']} (Estado actual: {elemento['estado']})")
            
            elemento["nombre"] = input(f"Nuevo nombre [{elemento['nombre']}]: ") or elemento["nombre"]
            
            elemento["categoria"] = input(f"Nueva categoría [{elemento['categoria']}]: ") or elemento["categoria"]
            
            elemento["cantidad"] = int(input(f"Nueva cantidad [{elemento['cantidad']}]: ") or elemento["cantidad"])
            
            elemento["valor"] = float(input(f"Nuevo valor [{elemento['valor']}]: ") or elemento["valor"])
            
            print("Estados: activa, inactiva, en reparacion, fuera de servicio: ")
            
            elemento["estado"] = input(f"Nuevo estado [{elemento['estado']}]: ").lower() or elemento["estado"]
            
            guardar_json(RUTA, herramientas)
            print("Herramienta actualizada ")
            return
    print("no encontrada.")


def eliminar_herramienta():
    herramientas = cargar_json(RUTA)
    id_buscar = int(input("ID herramienta: "))
    for h in herramientas:
        if h["id"] == id_buscar:
            h["estado"] = "inactiva"
            guardar_json(RUTA, herramientas)
            print("Herramienta inactivada.")
            return
    print("No encontrada.")

def actualizar_stock(id_herramienta, cantidad):
    herramientas = cargar_json(RUTA)
    for h in herramientas:
        if h["id"] == id_herramienta:
            h["cantidad"] += cantidad
            guardar_json(RUTA, herramientas)
            return

def obtener_herramienta(id_herramienta):
    herramientas = cargar_json(RUTA)
    for h in herramientas:
        if h["id"] == id_herramienta:
            return h
    return None


