"""
Autor: Regina N. Molares
Fecha: Diciembre 2025
Parte del paquete: dataset-quality-validator
- inspect_data.py
- interpretar_report.py
- JSON generado
- Reporte TXT
- Ejecución con IA local (LM Studio con nous-hermes-2-mistral-7b-dpo)
Descripción: Script que analiza datasets localmente, genera JSON de información y produce reportes TXT usando IA local (LM Studio).
Repositorio: https://github.com/programming-Regina/dataset-quality-validator
"""

import json
import requests

# --- Configuración ---
ruta_reporte = "reporte_validacion.json"
url_modelo = "http://localhost:1234/v1/chat/completions"
modelo = "local-model"

# --- Carga del reporte ---
with open(ruta_reporte, "r", encoding="utf-8") as archivo:
    reporte = json.load(archivo)

# --- Construcción del prompt ---
prompt = f"""
Sos un analista de datos senior que interpreta reportes de validación de datasets.

Reglas estrictas de salida:
- No expliques conceptos básicos de ciencia de datos.
- No repitas información ya incluida en el reporte.
- Evitá introducciones genéricas y frases vagas.
- Usá frases cortas y directas.
- Máximo 3 secciones.
- Máximo 4 bullets por sección.
- No uses tono pedagógico ni narrativo.

Reporte de validación:
- Decisión: {reporte['decision']}
- Columnas con problemas: {reporte['columnas_con_problemas']}
- Umbral de valores nulos permitido: {reporte['umbral_nulos']}

Formato obligatorio de salida:

Decisión:
<una sola línea>

Impacto:
<1 a 2 líneas>

Acciones recomendadas:
- <acción concreta>
- <acción concreta>
- <acción concreta>

No agregues texto fuera de este formato.
"""


# --- Llamada al modelo local ---
respuesta = requests.post(
    url_modelo,
    headers={"Content-Type": "application/json"},
    json={
        "model": modelo,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.3
    }
)

contenido = respuesta.json()["choices"][0]["message"]["content"]

# --- Salida ---
ruta_salida = "interpretacion_reporte.txt"

with open(ruta_salida, "w", encoding="utf-8") as archivo:
    archivo.write("INTERPRETACIÓN AUTOMÁTICA DEL REPORTE\n")
    archivo.write("=" * 40 + "\n\n")
    archivo.write(contenido)

print("\n--- Interpretación del reporte ---\n")
print(contenido)
print(f"\nInterpretación guardada en: {ruta_salida}")
