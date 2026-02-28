from os import system
from pathlib import Path

def limpir_pantalla():
    system("clear")

def contar_recetas(mi_ruta):

    cantidad_de_recetas = 0

    for _ in mi_ruta.glob("**/*.txt"):
        cantidad_de_recetas += 1

    return cantidad_de_recetas

def pedir_opcion():

    opciones = ['1.leer recetas', '2.crear recetas', '3.crear categoría', '4.eliminar receta', '5.eliminar categoría', '6.finalizar progama']

    opcion_valida = False

    eleccion = 0

    while not opcion_valida:
        eleccion = input(f"elige una opción del 1 al 6: {opciones}: ")

        if not eleccion.isdigit():
            print("Debe elegir un NUMERO del 1 al 6")
            continue
        eleccion = int(eleccion)

        if eleccion not in range(1, 7):
            print("El numero elegido no se encuentra en el rango, elija un numero del 1 al 6")
            continue

        opcion_valida = True

    return eleccion

def elegir_categoria(mi_ruta):

    lista_categorias = []
    lista_categorias_user = []

    for _ in mi_ruta.iterdir():
        if _.is_dir():
            lista_categorias.append(_.name)
            lista_categorias_user.append(_)

    lista_categorias.sort()
    lista_categorias_user.sort()

    categoria_valida = False
    categoria_elegida = 0

    while not categoria_valida:
        categoria_elegida = input(f"Elige una categoria del 1 al {len(lista_categorias)} {lista_categorias}: ").strip()

        if  categoria_elegida.isdigit() == False:
            print(f"Debes elegir un numero del 1 al {len(lista_categorias)}")
            continue

        categoria_elegida = int(categoria_elegida)

        if categoria_elegida not in range(1, (len(lista_categorias) + 1)):
            print(f"Debes elegir un numero del 1 al {len(lista_categorias)}")
            continue


        categoria_valida = True


    return lista_categorias_user[categoria_elegida -1]

def elegir_receta(ruta_categoria):

    lista_receta = []
    lista_receta_user = []

    ruta_ds = ruta_categoria / ".DS_Store"
    if ruta_ds.exists():
        ruta_ds.unlink()

    for _ in ruta_categoria.iterdir():
        if _.is_file() and _.suffix == ".txt":
            lista_receta.append(_.name)
            lista_receta_user.append(_)

    lista_receta.sort()
    lista_receta_user.sort()

    if len(lista_receta) == 0:
        print("Esta categoría no tiene recetas todavía.")
        return None

    receta_valida = False
    receta_elegida = None

    while not receta_valida:
        receta_elegida = input(f"Elije la receta utilizando un numero del 1 al {len(lista_receta)} {lista_receta}: ")

        if receta_elegida.isdigit() == False:
            print(f"Debes el NUMERO del 1 al {len(lista_receta)}")
            continue

        receta_elegida = int(receta_elegida)

        if receta_elegida not in range(1, (len(lista_receta) + 1)):
            print(f"Debes elegir dentro del rango, elige un numero del 1 al {len(lista_receta)}")
            continue


        receta_valida = True

    return lista_receta_user[receta_elegida - 1]

def leer_receta (ruta_receta):
    if not ruta_receta.exists():
        print("La receta no existe")
    else:
        print(ruta_receta.read_text())

def eliminar_receta(ruta_receta):

    if not ruta_receta.exists():
        print("La ruta a esta receta no existe")
    elif not ruta_receta.suffix == ".txt":
        print("La ruta a esta receta no es TXT")
    else:
        ruta_receta.unlink()
        print(f"Receta eliminada")

def crear_receta(ruta_categoria):

    nombre_valido = False
    nombre = " "


    while not nombre_valido:
        nombre = input("Ingresa el nombre de tu receta: ").strip()

        if nombre == "":
            print("Debes escribir algo para poder crear una receta")
            continue

        if Path(ruta_categoria, nombre + ".txt").exists():
            print("Ya existe el nombre de la receta en esta carpeta \npor favor, elija otro nombre: ")
            continue

        nombre_valido = True

    ruta_receta_nueva = Path(ruta_categoria, nombre + ".txt")

    lineas = []
    print("Escribe el contenido. Para terminar, deja una línea vacía y presiona Enter.")

    while True:
        linea = input().strip()
        if linea == "".strip():
            break
        lineas.append(linea)

    contenido = "\n".join(lineas)

    ruta_receta_nueva.write_text(contenido, encoding="utf-8")

    return ruta_receta_nueva

def crear_categoria(ruta_principal):

    nombre_valido = False
    ruta_nueva_categoria = None
    nombre_categoria = ' '

    while not nombre_valido:
        nombre_categoria = input("Escriba el nombre de la categoria que desea crear: ").strip()

        if nombre_categoria == '':
            print("El nombre no puede estar vacio")
            continue

        nombre_valido = True

    if Path(ruta_principal, nombre_categoria).exists():
        print("Esta categoria ya existe")
    else:
        ruta_nueva_categoria = Path(ruta_principal, nombre_categoria)
        ruta_nueva_categoria.mkdir()

    return ruta_nueva_categoria

def eliminar_categoria(categoria_elegida):

    lista = []

    for _ in categoria_elegida.iterdir():
        lista.append(_)

    if not categoria_elegida.exists():
        print("Esta categoria no existe")
    elif not lista == []:
        print("La categoria tiene elementos dentro, por seguridad no se puede eliminar")
    else:
        categoria_elegida.rmdir()
        print(f"Categoria eliminada: {categoria_elegida.name}")
