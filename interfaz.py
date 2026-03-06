from gestionarusuario import login, agregar_usuario, listar_usuarios, actualizar_usuarios, eliminar_usuarios,buscar_usuarios

from gestionarherramientas import agregar_herramienta,listar_herramientas,eliminar_herramienta,actualizar_herramienta


from gestionarprestamos import crear_solicitud,aprobar_solicitud,devolver_prestamo,reporte_stock,consultar_quien_tiene,herramientas_frecuentes,consultar_quien_tiene,historial_usuario,reporte_prestamos_vencidos



def menu_principal():
    usuario = login()
    if not usuario:
        return

    while True:

        if usuario["tipo"] == "administrador":
            print("""
1. Agregar herramienta
2. Listar herramientas
3. actualizar herramientas
4. Inactivar herramienta
5. Agregar usuario
6. Listar usuarios
7. actualizar usuario
8. buscar usuario
9. eliminar usuarios
10. Aprobar solicitud
11. Devolver préstamo
12. Reporte stock bajo
13. ver historial de algun usuario
14. herramientas mas pedidas
15. quien tiene una herramienta
16. prestamos vencidos
17. Salir
""")

            op = input("Opción: ")

            match op:
                case "1":
                    agregar_herramienta()
                case "2":
                    listar_herramientas()
                case "3":
                    actualizar_herramienta()
                case "4":
                    eliminar_herramienta()
                case "5":
                    agregar_usuario()
                case "6":
                    listar_usuarios()
                case "7":
                    actualizar_usuarios()
                case "8":
                    buscar_usuarios()
                case "9":
                    eliminar_usuarios()
                case "10":
                    aprobar_solicitud()
                case "11":
                    devolver_prestamo()
                case "12":
                    reporte_stock()
                case "13":
                    historial_usuario()
                case "14":
                    herramientas_frecuentes()
                case "15":
                    consultar_quien_tiene()
                case "16":
                    reporte_prestamos_vencidos()
                case "17":
                    break
                case _:
                    print("Opción inválida")

        else:
            print("""
1. Listar herramientas
2.consultar quien posee una herramienta
3. Crear solicitud
4. Salir
""")
            op = input("Opción: ")

            match op:
                case "1":
                    listar_herramientas()
                case "2":
                    consultar_quien_tiene()
                case "3":
                    crear_solicitud(usuario)
                case "4":
                    break
                case _:
                    print("Opción inválida")



