import pandas as pd

df_ventas = pd.read_csv('ventas.csv', sep=';')

print(df_ventas.head())

df_ventas.fillna(0, inplace=True)

print(" ")

df_ventas['Ingresos'] = df_ventas['Cantidad'] * df_ventas['Precio_Unitario']

print(df_ventas.head())

print(" ")

ingreso_por_tienda_producto = df_ventas.groupby(['Tienda', 'Producto'])['Ingresos'].sum().reset_index()

print(ingreso_por_tienda_producto)

print(" --- --- --- --- --- --- --- --- --- --- --- --- --- ---")

top_productos = ingreso_por_tienda_producto.sort_values(['Tienda', 'Ingresos'], ascending=[True, False]).groupby('Tienda').first().reset_index()

print(top_productos)

print(" ")

resumen_cantidad=df_ventas.groupby('Producto')['Cantidad'].sum().reset_index()

print(resumen_cantidad)

#GuardarCSV
def csv():
    resumen_cantidad.to_cvs('Resumen_ventas.csv', index=False)

csv()

    








