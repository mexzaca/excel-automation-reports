import pandas as pd

# Cargar archivo Excel
file_path = "data/datos.xlsx"  # Ruta del archivo de Excel
df = pd.read_excel(file_path, engine="openpyxl")

# Mostrar las primeras filas del archivo
print("Primeras filas del archivo:")
print(df.head())

# Guardar un reporte filtrado en la carpeta reports/
filtered_df = df[df["Columna1"] > 100]  # Ejemplo de filtro
filtered_df.to_excel("reports/reporte_filtrado.xlsx", index=False)

print("Reporte generado en reports/reporte_filtrado.xlsx")
