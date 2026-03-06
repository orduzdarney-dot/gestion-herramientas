
from gestionarjson import cargar_json, guardar_json


RUTA = "usuarios.json"

def generar_id(lista):
    return 1 if not lista else lista[-1]["id"] + 1

def agregar_usuario():
    usuarios = cargar_json(RUTA)
    nombres = input("Nombres: ")
    apellidos = input("Apellidos: ")
    telefono = input("Teléfono: ")
    direccion = input("Dirección: ")
    tipo = input("Tipo (administrador/usuario): ").lower()

    nuevo = {
        "id": generar_id(usuarios),
        "nombres": nombres,
        "apellidos": apellidos,
        "telefono": telefono,
        "direccion": direccion,
        "tipo": tipo
    }

    if tipo == "administrador":
        nuevo["password"] = input("contraseña: ")

    usuarios.append(nuevo)
    guardar_json(RUTA, usuarios)
    print("Usuario agregado.")

def login():
    usuarios = cargar_json(RUTA)
    nombre_ingresado = input("Ingrese su nombre: ").strip().lower()

    for u in usuarios:
        
        if u["nombres"].strip().lower() == nombre_ingresado:
            if u["tipo"] == "administrador":
                clave = input("Ingrese contraseña: ").strip() 
                
                
                password_guardada = str(u.get("password", u.get("password", ""))).strip()
                
                if password_guardada == clave:
                    print(f"Bienvenido {u['nombres']}")
                    return u
                else:
                    print("Contraseña incorrecta.")
                    return None
            
           
            print(f"Bienvenido {u['nombres']}")
            return u

    print("Usuario no encontrado.")
    return None


def listar_usuarios():
    usuarios = cargar_json(RUTA)
    print("\n--- LISTA DE USUARIOS ---")
    print("ID\tNOMBRE\t\tAPELLIDO\tTIPO")
    print("-" * 50)
    
    for u in usuarios:
        print(f"{u['id']}\t{u['nombres']}\t\t{u['apellidos']}\t{u['tipo']}")




def buscar_usuarios():
    usuarios = cargar_json(RUTA)
    id_buscar = int(input("Ingrese el ID del usuario a buscar: "))
    for u in usuarios:
        if u["id"] == id_buscar:
            print(f"\nUsuario encontrado: {u['nombres']} {u['apellidos']}")
            print(f"Teléfono: {u['telefono']} | Dirección: {u['direccion']} | Tipo: {u['tipo']}")
            return u
    print("Usuario no encontrado.")
    return None

def actualizar_usuarios():
    usuarios = cargar_json(RUTA)
    id_buscar = int(input("Ingrese el ID del usuario a actualizar: "))
    for u in usuarios:
        if u["id"] == id_buscar:
            print(f"Modificando a: {u['nombres']}")
            
            u["nombres"] = input(f"Nuevos nombres [{u['nombres']}]: ") or u["nombres"]
            
            u["apellidos"] = input(f"Nuevos apellidos [{u['apellidos']}]: ") or u["apellidos"]
            
            u["telefono"] = input(f"Nuevo teléfono [{u['telefono']}]: ") or u["telefono"]
            
            u["direccion"] = input(f"Nueva dirección [{u['direccion']}]: ") or u["direccion"]
            
            guardar_json(RUTA, usuarios)
            print("Datos del usuario actualizados ")
            return
    print("usuario no encontrado")

def eliminar_usuarios():   
    
    usuarios = cargar_json(RUTA)
    id_buscar = int(input("Ingrese el ID del usuario a eliminar: "))
    for i, u in enumerate(usuarios):
        if u["id"] == id_buscar:
            confirmar = input(f"¿Seguro que desea eliminar a {u['nombres']}? : ")
            if confirmar.lower() == 's':
                usuarios.pop(i)
                guardar_json(RUTA, usuarios)
                print("usuario eliminado del sistema")
            return
    print("usuario no encontrado")
    
    
    
