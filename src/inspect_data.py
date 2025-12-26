import pandas as pd
import json
from datetime import datetime

# --- Configuración ---
ruta_csv = "data/adult.csv"
ruta_salida = "reporte_validacion.json"
umbral_nulos = 0.05  # 5%

# --- Carga del dataset ---
df = pd.read_csv(ruta_csv, na_values="?")

total_filas = len(df)
total_columnas = df.shape[1]

# --- Selección de columnas categóricas ---
columnas_categoricas = df.select_dtypes(include="object").columns

# --- Cálculo de valores nulos ---
reporte_nulos = {}

for columna in columnas_categoricas:
    cantidad_nulos = df[columna].isna().sum()
    proporcion_nulos = cantidad_nulos / total_filas
    reporte_nulos[columna] = round(proporcion_nulos, 4)

# --- Evaluación ---
columnas_con_problemas = {
    col: prop
    for col, prop in reporte_nulos.items()
    if prop > umbral_nulos
}

decision = "REVISAR" if columnas_con_problemas else "APTO"

# --- Construcción del reporte ---
reporte = {
    "fecha_ejecucion": datetime.now().strftime("%Y-%m-%d %H:%M"),
    "filas": total_filas,
    "columnas": total_columnas,
    "umbral_nulos": umbral_nulos,
    "valores_nulos": reporte_nulos,
    "columnas_con_problemas": columnas_con_problemas,
    "decision": decision
}

# --- Guardado del reporte ---
with open(ruta_salida, "w", encoding="utf-8") as archivo:
    json.dump(reporte, archivo, indent=4, ensure_ascii=False)

# --- Salida por consola ---
print("Evaluación del dataset\n")
print(f"Filas: {total_filas}")
print(f"Columnas: {total_columnas}\n")

print("Valores nulos por columna categórica:")
for col, prop in reporte_nulos.items():
    print(f"- {col}: {prop:.2%}")

print("\nResultado:")
print(f"DECISIÓN: {decision}")
print(f"\nReporte generado en: {ruta_salida}")
