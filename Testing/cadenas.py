""" Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en 
líneas distintas el nombre del usuario tantas veces como el número introducido.
"""

nombre = input("Introduce un nombre: ")
num = input("Cuantas veces ha de repertirse: ")

print((nombre + " \n")*int(num))


""" Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla el nombre completo 
del usuario tres veces, una con todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la primera letra del nombre
 y de los apellidos en mayúscula.
 El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera."""


name = input( "Introduce tu nombre: ")

mayus = name.upper()
minus = name.lower()
prim = name.capitalize()

print(mayus + " \n" + minus + " \n" + prim)


"""Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla
 <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre.


"""

nom = input("Introduce un nombre: ")
print(nom.upper() + " tiene " + str(len(nom)) + " letras.")

