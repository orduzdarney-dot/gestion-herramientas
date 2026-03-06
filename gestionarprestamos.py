

from gestionarjson import cargar_json, guardar_json
from gestionarherramientas import obtener_herramienta, actualizar_stock
from datetime import datetime

RUTA_PRESTAMOS = "prestamos.json"
RUTA_SOLICITUDES = "solicitudes.json"

def generar_id(lista):
    return 1 if not lista else lista[-1]["id"] + 1

def registrar_log(mensaje):
    with open("logs.txt", "a") as archivo:
        archivo.write(f"{datetime.now()} - {mensaje}\n")

def crear_solicitud(usuario):
    solicitudes = cargar_json(RUTA_SOLICITUDES)
    nueva = {
        "id": generar_id(solicitudes),
        "id_usuario": usuario["id"],
        "id_herramienta": int(input("ID herramienta: ")),
        "cantidad": int(input("Cantidad: ")),
        "fecha": str(datetime.now()),
        "estado": "pendiente"
    }
    solicitudes.append(nueva)
    guardar_json(RUTA_SOLICITUDES, solicitudes)
    print("Solicitud creada.")

def aprobar_solicitud():
    solicitudes = cargar_json(RUTA_SOLICITUDES)
    prestamos = cargar_json(RUTA_PRESTAMOS)
    id_solicitud = int(input("ID solicitud: "))

    for s in solicitudes:
        if s["id"] == id_solicitud and s["estado"] == "pendiente":
            herramienta = obtener_herramienta(s["id_herramienta"])
            
            if not herramienta or herramienta["cantidad"] < s["cantidad"]:
                print("Stock insuficiente o herramienta no existe.")
                registrar_log("Intento de préstamo sin stock o ID inválido.")
                return

            actualizar_stock(s["id_herramienta"], -s["cantidad"])

            nuevo_prestamo = {
                "id": generar_id(prestamos),
                "id_usuario": s["id_usuario"],
                "id_herramienta": s["id_herramienta"],
                "cantidad": s["cantidad"],
                "fecha_inicio": str(datetime.now()),
                "fecha_estimada": input("Fecha estimada devolución (YYYY-MM-DD): "),
                "estado": "activo",
                "observaciones": input("Observaciones: ")
            }

            prestamos.append(nuevo_prestamo)
            s["estado"] = "aprobada"
            guardar_json(RUTA_PRESTAMOS, prestamos)
            guardar_json(RUTA_SOLICITUDES, solicitudes)
            print("Solicitud aprobada.")
            return
    print("Solicitud no encontrada.")

def devolver_prestamo():
    prestamos = cargar_json(RUTA_PRESTAMOS)
    id_buscar = int(input("ID préstamo: "))
    for p in prestamos:
        if p["id"] == id_buscar and p["estado"] == "activo":
            p["estado"] = "devuelto"
            actualizar_stock(p["id_herramienta"], p["cantidad"])
            guardar_json(RUTA_PRESTAMOS, prestamos)
            print("Devuelto.")
            return
    registrar_log(f"Herramienta ID {p['id_herramienta']} devuelta por Usuario ID {p['id_usuario']}")
    print("Préstamo no encontrado.")

def reporte_stock():
    
    
    herramientas = cargar_json("herramientas.json")
    for h in herramientas:
        if h["cantidad"] < 3:
            print(h)

def prestamos_activos():
    prestamos = cargar_json(RUTA_PRESTAMOS)
    for p in prestamos:
        if p["estado"] == "activo":
            print(p)


def consultar_quien_tiene():
    
    prestamos = cargar_json(RUTA_PRESTAMOS)
    herramientas = cargar_json("herramientas.json")
    usuarios = cargar_json("usuarios.json")
    
    id_herramienta = int(input("Ingrese el ID de la herramienta que busca: "))
    
   
    nom_herramienta = next((h["nombre"] for h in herramientas if h["id"] == id_herramienta), "Desconocida")
    
    print(f"\n--- RASTREO DE: {nom_herramienta.upper()} ---")
    encontrado = False
    
    for p in prestamos:
        
        if p ["id_herramienta"] == id_herramienta and p ["estado"] == "activo":
            
            vecino = next((u["nombres"] for u in usuarios if u["id"] == p ["id_usuario"]), "Alguien")
            print(f"El vecino '{vecino}' tiene {p ['cantidad']} unidad(es).")
            print(f"Fecha estimada de devolución: {p ['fecha_estimada']}")
            print("-" * 30)
            encontrado = True
            
    if not encontrado:
        print("No hay préstamos activos para esta herramienta.")
        
        
def herramientas_frecuentes():
    prestamos = cargar_json("prestamos.json")
    herramientas = cargar_json("herramientas.json")

    print("\n--- Herramientas más pedidas ---")

    for h in herramientas:
        contador = 0
        
        for p in prestamos:
            if p["id_herramienta"] == h["id"]:
                contador = contador + 1
        
        
        if contador > 0:
            print(f"La herramienta '{h['nombre']}' se ha pedido {contador} veces.")
            
            
def consultar_quien_tiene():
    prestamos = cargar_json("prestamos.json")
    usuarios = cargar_json("usuarios.json")
    id_herramienta = int(input("ID de la herramienta : "))

    print("--- Buscando quién la tiene actualmente ---")
    encontrado = False

    for p in prestamos:
        
        if p["id_herramienta"] == id_herramienta and p["estado"] == "activo":
            
            for u in usuarios:
                if u["id"] == p["id_usuario"]:
                    print(f"La tiene el vecino: {u ['nombres']}")
                    print(f"Debe devolverla el: {p ['fecha_estimada']}")
                    encontrado = True

    if encontrado == False:
        print("nadie tiene esta herramienta en préstamo ahora mismo.")

        
def historial_usuario():
    prestamos = cargar_json("prestamos.json")
    id_usuario = int(input("¿ID del vecino a consultar?: "))
    
    print(f"--- Historial del Vecino {id_usuario} ---")
    encontrado = False
    
    for p in prestamos:
        if p["id_usuario"] == id_usuario:
            print(f"Prestó herramienta {p['id_herramienta']} el día {p['fecha_inicio']}")
            encontrado = True
            
    if encontrado == False:
        print("Este vecino no ha pedido nada aún.")   
        
        
def reporte_prestamos_vencidos():
    prestamos = cargar_json(RUTA_PRESTAMOS)
    usuarios = cargar_json("usuarios.json")
    
    hoy = str(datetime.now())[:10] 

    print(f"\n--- PRÉSTAMOS VENCIDOS - Fecha de hoy: {hoy}) ---")
    encontrado = False

    for p in prestamos:
        
        if p["estado"] == "activo" and p["fecha_estimada"] < hoy:
            
            nombre_usuario = "Desconocido"
            for u in usuarios:
                if u["id"] == p["id_usuario"]:
                    nombre_usuario = u["nombres"]
            
            print(f" El vecino {nombre_usuario} debía devolver la herramienta el {p['fecha_estimada']}")
            encontrado = True
    
    if not encontrado:
        print("no hay préstamos vencidos por ahora")
        
        
def usuarios_mas_activos():
    prestamos = cargar_json(RUTA_PRESTAMOS)
    usuarios = cargar_json("usuarios.json")
    
    print("--- Vecinos más activos  ---")
    for u in usuarios:
        contador = 0
        for p in prestamos:
            if p["id_usuario"] == u["id"]:
                contador += 1
        if contador > 0:
            print(f"El vecino {u['nombres']} ha realizado {contador} préstamos.")