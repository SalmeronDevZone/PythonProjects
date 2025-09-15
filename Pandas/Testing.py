import numpy as np

def funciones1():

    lista1 = [1,2,3,4,5,6,4,21,2,2,6,7,82,2,34]

    array1 = np.array(lista1)

    print(type(array1))
    print(lista1)
    print(array1)

    lista2 = [[1,2,3],[4,5,6],[7,8,9]]

    array2 = np.array(lista2)

    print(lista2)
    print(array2)



    array2 = np.arange(2, 27, 3)
    # Desde el numero dos hasta el 27 en intervalos de 3.
    print(array2)

    matrizZeros = np.zeros  ( (3,4) )
    # 4 filas y 3 columnas de ceros.
    print(matrizZeros)

    matrizUnos = np.ones((5,10))
    print(matrizUnos)

def funciones2():

    #Matriz con valores de 2 al 6
    matriz3 = np.linspace(2,6,40)

    #Matriz identadad
    matrizIdentidad= np.eye(7)
    print(matrizIdentidad)

    #MatrizAleatoria
    MatrizAleatoria = np.random.rand(3,4)

    #OtraAleatoria

    matrizAleatoriaEnteros = np.random.randint(1,51,20)
    print(matrizAleatoriaEnteros)

    array = np.random.randint(1,900,200)
    maximo = array.max()
    minimo = array.min()

    print(f"El valor maximo es {maximo}")
    print(array.argmax())   #Indica la posición última.

    array = np.arange(1,11)
    print(array)
    print(array[2])










