#Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

edad = int(input("Introduce tu edad : "))

if edad <18:
    print("Es menos de edad.")
else :
    print("Es mayor de edad.")


""""Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por
 pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas."""

passw = "Contraseña"
entrada = input("Introduce la contraseña : ")

password = passw.lower()

if password == entrada:
    print("Contraseña correcta")
else:
    print("Fallaste.")


# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

numero = int(input("Introduce un numero: "))

if numero % 2 == 0:
    print("Es numero par")
else:
    print("Es impar.")


"""Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un 
programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no."""


edad = int(input("Introduce la edad del sujeto. "))
ingresos = int(input("Introduce los ingresos del sujeto. "))

if edad > 15 and ingresos > 1000:
    print("Debe tributar.")
else:
    print("No debe tributar.")



"""Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con
 un nombre anterior a la M y los hombres con un nombre posterior a la N 
y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde."""

name = input("Introduce tu nombre:")
sexo = input("Introduce tu sexo: m-f : ")

if (sexo == "f" and name.lower() > "m") or (sexo == "m" and name.lower() < "n"):
    print("Deben ir al grupo A")
else:
    print("Deben ir al grupo B.")


# Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.

"""Menos de 10000€	5%
Entre 10000€ y 20000€	15%
Entre 20000€ y 35000€	20%
Entre 35000€ y 60000€	30%
Más de 60000€	45%"""

tasa = float(input("Introduzca su renta: "))

if tasa < 10000:
    print("Debe pagar 5%")
elif tasa >= 10000 and tasa < 20000:
    print("Debe pagar 15%")
elif tasa >= 20000 and tasa < 35000:
    print("Debe pagar 20%")
elif tasa >= 35000 and tasa < 60000:
    print("Debe pagar el 30%")
elif tasa > 60000:
    print("Debe pagar el 45%.")

"""En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación comienzan 
en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o 
más, pero no valores intermedios entre las cifras mencionadas. A continuación se muestra una tabla con los niveles
 correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel."""

bonificacion = 2400
inaceptable = 0
aceptable = 0.4
meritorio = 0.6
puntos = float(input("Introduce tu puntuación: "))

# Clasifiación por niveles de rendimiento

if puntos == inaceptable:
    nivel = "Inaceptable"
elif puntos == aceptable:
    nivel = "Aceptable"
elif puntos >= 0.6:
    nivel = "Meritorio"
else:
    nivel = ""

# Mostrar nivel de rendimiento

if nivel == "":
    print("Esta puntuación no es válida")
else:
    print("Tu nivel de rendimiento es %s" % nivel)
    print("Te corresponde cobrar %.2f€" % (puntos * bonificacion))



"""La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen
 a continuación.

Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los 
ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. 
Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva."""



#Presentación de pizzeria.

print("Bienvenido a la pizzeria Panuccis Elija -1- para piza vegetariana o -2- para pizza normal: \nCualquier otro número para salir:   ")

opcion = int(input("Escoja su menú. "))

if opcion == 1:     #Desarrollamos la opción vegetariana. Debe de elegir entre las dos opciones o el programa le dará error.

    print("Ingredientes Vegetarianos: \n 1 - Pimiento \n 2 - Tofu") #Tofu en una pizza????
    a = int(input("Introduzca su opción: "))

    while (a != 1) and (a != 2):
        print("Opción equivocada.Repita su respuesta.")
        a = int(input("Introduzca su opción: "))
        


    if a == 1:
        print("Los ingredientes de su pizza son tomate, mozarrella y pimiento, menos mal que no has pedido el tofu.")
    elif a == 2:
        print("Los ingredientes son tomate, mozarrella y tu querido tofu.")
    else:
        print("No has elegido una opción correcta.")

elif opcion == 2:

    print("Ingredientes NO Vegetarianos: \n 1 - Peperoni \n 2 - Jamón \n 3 - Salmón.") #Tofu en una pizza????
    b = int(input("Introduzca su opción: "))

    while (b != 1) and (b != 2) and (b != 3):
        print("Opción equivocada.Repita su respuesta.")
        b = int(input("Introduzca su opción: "))

    if b == 1:
        print("Los ingredientes de la pizza son tomate, mozarella y peperoni. ")
    elif b == 2:
        print("Los ingredientes de la pizza son tomate, mozarella y jamón. ")
    elif b == 3 :
        print("Los ingredientes de la pizza son tomate, mozarella y salmón. ")
    else :
        print("ERROR EN EL SISTEMA.") #  --> Gracias al bucle while, esta lina de código nunca se ejecutará. 

else :
    print("Gracias por su visita.")