"""Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'},
 pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si 
la divisa no está en el diccionario."""

def uno():

    currency = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
    choose = input("Escoga una moneda: ")
    choo = choose.capitalize()

    if choo in currency:
        print(currency[choo])
    else:
        print("Inserte una opción correcta.")

#uno ()

"""Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario.
 Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>."""

 
def dos():
   
   nombre = input("Introduzca su nombre: ")
   edad = int(input("Cual es su edad: "))

   while edad < 0 or edad > 99:
       print("Edad introducida no correcta.")
       edad = int(input("Cual es su edad: "))

   direccion = input("Introduce tu direccion: ")
   telefono = input("Introduce tu telefono: ") #Suelen ser 9 dígitos.
   
   while len(telefono) != 9:
       print("Deben ser 9 dígitos.")
       telefono = input("Introduce tu telefono: ")

   persona = {'nombre': nombre, 'edad': edad, 'dirección': direccion, 'telefono': telefono}
   print(persona['nombre'], 'tiene', persona['edad'], 'años, vive en', persona['direccion'], 'y su número de teléfono es', persona['telefono'])


#dos()

"""Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta,
 un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta.
   Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello."""


def fruteria():

    frutas ={'Platano':1.35, 'Manzana': 0.80, 'Pera':0.85, 'Naranja':0.70}
    fruta = input("Elige una fruta: ").title()
    kg = float(input("Cuantos kg: "))

    if fruta in frutas:     #Molaria mas un bucle while rollo....hasta que no me compres lo que tengo de la fruteria no sales.
        print(kg, "kilos de", fruta, "valen", frutas[fruta]*kg,"€")
    else:
        print("Fruta no disponible.")


#fruteria()


"""Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5}
 y después muestre por pantalla los créditos de cada asignatura en el formato <asignatura> tiene <créditos> créditos,
   donde <asignatura> es cada una de las asignaturas del curso, y <créditos> son sus créditos.
     Al final debe mostrar también el número total de créditos del curso."""

def creditos():

    curso = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
    total_creditos = 0

    for asignatura, creditos in curso.items():
        print("La", asignatura, "tiene",creditos,"creditos.")
        total_creditos += creditos
    print("numero total de creditos: ",total_creditos)


#creditos()


"""Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, 
teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario."""

def diccEmpty():

    persona = {}
    continuar = True
    while continuar:
        clave = input('¿Qué dato quieres introducir? ')
        valor = input(clave + ': ')
        persona[clave] = valor
        print(persona)
        continuar = input('¿Quieres añadir más información (Si/No)? ') == "Si"

#diccEmpty()