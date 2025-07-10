import pandas as pd

# Ruta del archivo CSV
csv_file = 'archivo.csv'

# Ruta del archivo Excel de salida
excel_file = 'archivo_convertido.xlsx'

# Leer el archivo CSV
df = pd.read_csv(csv_file)

# Guardar como archivo Excel
df.to_excel(excel_file, index=False)

print(f'Archivo convertido exitosamente: {excel_file}')
