import pandas as pd
import numpy as np

def Sample1():
    etiquetas = ['a','b','c','d','e']
    datos = np.arange(4,9)
    serie = pd.Series(datos, index=etiquetas)

    print(serie)

    #Accede Valor
    print(serie['c'])

    #Datos distinto tipo
    datos = ['Jose', 55, 'Mar', 46]
    serie = pd.Series(datos)
    print(serie)

    # datosDirectos
    serie = pd.Series([1000, 500, 1200, 700], index=['Emp01', 'Emp02', 'Emp03', 'Emp04'])
    print(serie)

    #OPERACION SUMAS
    serie1 = pd.Series([1000, 500, 1200, 700])
    serie2 = pd.Series([10230, 5400, 1200, 500])

    serie3 = serie1 + serie2
    print(serie3)


#DATA FRAMES

filas = ['tienda1', 'tienda2', 'tienda3', 'tienda4']
columnas = ['art1', 'art2', 'art3']
datos = [[np.nan,100,200], [np.nan,200,100], [np.nan,100,420], [np.nan,200,100]]

dataframe = pd.DataFrame(datos, index = filas, columns = columnas)
print(dataframe)

#Seleccion fila

print(dataframe.loc['tienda2'])


#Seleccion columna

print(dataframe['art3'])

#Nueva columna
dataframe ['total'] = dataframe['art1'] + dataframe['art2'] + dataframe['art3']
print(dataframe)

#Eliminar total
print(dataframe.drop(['total'], axis=1))        #EL DROP CON PRINT NO LO BORRA, PERO NO LA MUESTRA
"""✅ Con axis=1 borras columnas
✅ Con axis=0 borras filas"""


condicion = dataframe > 200
print(dataframe[condicion])     #NaN = not a number, es decir valor nulo.

condicion = (dataframe ['art1'] >= 300) & (dataframe['art2'] > 100)
print(dataframe[condicion])

nuevaColumna = '1 2 3 4'.split()
dataframe['Indices'] = nuevaColumna

print(dataframe)

dataframe = dataframe.set_index('Indices')
print(dataframe)

        #dataframe.dropna(axis=1, impace=True)   Se borran las columnas (axis = 1) donde hay nulos.

dataframe.fillna(value=0, inplace=True)


"""import pandas as pd

data = {'A': [1, None, 3], 'B': [None, 5, 6]}
df = pd.DataFrame(data)

df_filled = df.fillna(100)  # devuelve una copia con los NaN reemplazados
print(df)          # el DataFrame original NO cambia
print(df_filled)   # este sí tiene los NaN reemplazados
"""
"""
media = dataframe.mean()
print(f'la media es igual a {media}')
dataframe.fillna(value = media, inplace = True)

print(dataframe)
"""
print(dataframe)

data1 = dataframe.copy()
data2 = dataframe.copy()

dataTotal = pd.concat([data1, data2], axis = 0)
print(dataTotal)

print(dataTotal['art3'].value_counts())

print(dataTotal.index)
print(dataTotal.columns)

def ConvertirCSV():

    dataTotal.to_csv("dataTotal.csv")

def LeerCSV():

    dataframe = pd.read_csv("dataTotal.csv", index_col = 0)
    print(dataframe)


