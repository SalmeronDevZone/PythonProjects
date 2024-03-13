"""Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua)
 en una lista y la muestre por pantalla.

"""

def asignatura():

    asignaturas = ["Mates" , "Física" , "Química" , "Histoaria" , "Lengua"]
    print (asignaturas)

#asignatura()


"""Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.

"""

def estudios ():
    
    asignaturas = ["Mates" , "Física" , "Química" , "Histoaria" , "Lengua"]

    for i in asignaturas:
        print("Yo estudio ", i , end=" . ")

#estudios()


"""Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista,
 pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado
   <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el
     usuario."""


def nota():
     
    asignaturas = ["Mates" , "Física" , "Química" , "Histoaria" , "Lengua"]
    notas = []
    
    for i in asignaturas:
        nota = input("Que nota has sacado en " + i + "?  ")
        notas.append(nota)
    for z in range(len(asignaturas)):
        print("En ", asignaturas[z] + "has sacado un "+ notas[z])

#nota()

"""Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista 
y los muestre por pantalla ordenados de menor a mayor."""

def loterias():

    sorteo = []

    for i in range(6):
        num = int(input("Inserte el número premiado: "))
        sorteo.append(num)

    ordenados = sorted(sorteo)
    print(ordenados)

#loterias()

"""Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista,
 pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas.
   Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir."""


def Aprob():

    subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
    passed = []

    for subject in subjects:
        score = float(input("¿Qué nota has sacado en " + subject + "? "))
        if score >= 5:
            passed.append(subject)
            
    for subject in passed:
        subjects.remove(subject)
    print("Tienes que repetir " + str(subjects))

#Aprob()

