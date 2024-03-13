"""Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces."""

abc = input("Escribe una palabra que se repetirá 10 veces: ")

for i in range (9):
    print(abc,end=' ')

abcd = input("\nEscribe una palabra que se repetirá 10 veces: ")

contador = 1
while contador < 11:
    print(contador , abcd)
    contador = contador + 1


"""Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad)."""

edad = int(input("Introduce tu edad: "))

for z in range(edad):

    if z == 0:
            print ("Has cumplido", str(z+1) , " año.")
    else:
            print ("Has cumplido", str(z+1) , " años.")

    

"""Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta
 cero separados por comas."""

num = int(input("Introduce un número: "))

for i in range(num, -1 , -1):
      print(i,end=",")


"""Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo,
 de altura el número introducido.

*
**
***
****
***** 
        """


n = int(input("Cual será la altura del triángulo: "))

for i in range(n):
    for j in range(i+1):
        print("*", end="")
    print("")


"""Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10."""

for i in range(1,11):
    for j in range(1,11):
         print(i*j, end="\t")
    print("")


"""Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
 pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta."""


contras= "CONTRASEÑA"

passw = input("Introduzca una contraseña: ")
pas = passw.upper()

while pas != contras:
    print("contraseña incorrecta.")
    passw = input("Vuelva a intentarlo: ")
    pas = passw.upper()


print("Contraseña correcta.")


"""Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla
 el número de veces que aparece la letra en la frase."""


word = input("Introduce una palabra: ")
for i in range(len(word)-1, -1, -1):
    print(word[i])


"""Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba 
“salir” que terminará."""


while True:
    eco = input("Introduce la palabra salir , para salir del bucle.")

    if eco == "salir":
        break
    print(eco)

#CREAR UN CÓDIGO QUE SI INTRODUCES UNA PALABRA IMPRIMA TODAS LAS CONVINACIONES POSIBLES ENTRE SUS LETRAS :


texto = "aeiou"

diccionario = {}

for letra1 in texto:
    for letra2 in texto:
        for letra3 in texto:
            for letra4 in texto:
                clave = letra1 + letra2 + letra3 + letra4
                diccionario[clave] = ""
for clave in diccionario:
    print(clave)
