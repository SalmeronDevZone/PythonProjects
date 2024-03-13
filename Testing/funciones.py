"""Escribir una función que muestre por pantalla el saludo ¡Hola amiga! cada vez que se la invoque."""

def hola():
    return "Hola Mundo!!!"

saludo = hola()
#print(saludo)

"""Escribir una función a la que se le pase una cadena <nombre> y muestre por pantalla el saludo ¡hola <nombre>!."""

def hola2():
    persona = input("Introduce el nombre: ")
    print(f"HOLA {persona}!!")

hola2()