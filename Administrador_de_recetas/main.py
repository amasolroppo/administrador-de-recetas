from pathlib import Path
from os import system
from funciones import *

#Inserta tu propia ruta
ruta = Path(Path.home(), "Desktop", "PythonProject" ,"Python-alternativo", "Recetas")
print(ruta)

nombre = input("Ingresa el nombre: ")

while True:
    print(f"Hola {nombre}, bienvenido al administrador de recetas.")
    print(f"La ruta de acceso es: {ruta}")
    print(f"El total de recetas es: {contar_recetas(ruta)}")

    opcion_del_usuario = pedir_opcion()

    if opcion_del_usuario == 1:
        limpir_pantalla()
        categoria = elegir_categoria(ruta)
        receta_a_leer = elegir_receta(categoria)
        if receta_a_leer is None:
            continue
        leer_receta(receta_a_leer)

    elif opcion_del_usuario == 2:
        categoria = elegir_categoria(ruta)
        crear_receta(categoria)
        limpir_pantalla()
        print("Receta creada correctamente")

    elif opcion_del_usuario == 3:
        crear_categoria(ruta)
        limpir_pantalla()
        print("Categoria creada correctamente")

    elif opcion_del_usuario == 4:
        categoria = elegir_categoria(ruta)
        receta_a_eliminar = elegir_receta(categoria)
        eliminar_receta(receta_a_eliminar)
        limpir_pantalla()
        print("Receta eliminada correctamente")

    elif opcion_del_usuario == 5:
        categoria = elegir_categoria(ruta)
        eliminar_categoria(categoria)
        limpir_pantalla()
        print("Categoria eliminada correctamente")

    else:
        limpir_pantalla()
        print(f"Administrador de recetas cerrado. Adios {nombre} :)")
        break





