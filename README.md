# Dataset Validator con Interpretación mediante IA Local

## Descripción general

Este proyecto presenta un ejemplo completo y accesible de un flujo de trabajo para la validación inicial de datasets, incorporando interpretación automática de resultados mediante un modelo de lenguaje ejecutado en entorno local.

El objetivo no es automatizar el análisis de datos ni reemplazar decisiones humanas, sino mostrar cómo estructurar un proceso claro, reproducible y responsable en etapas tempranas de un proyecto de análisis.

---

## Problema que aborda

En la práctica profesional, la validación inicial de datos suele realizarse de manera informal o implícita.  
Este proyecto propone una alternativa estructurada que permite:

- detectar problemas básicos de calidad de datos
- documentar decisiones
- separar reglas automáticas de interpretación humana
- generar evidencia reutilizable

---

## Alcance del sistema

El sistema realiza las siguientes tareas:

1. Analiza un dataset en formato CSV
2. Evalúa valores nulos en columnas categóricas
3. Aplica un umbral configurable
4. Toma una decisión automática:
   - **APTO**
   - **REVISAR**
5. Genera un reporte estructurado en formato JSON
6. Utiliza un modelo de lenguaje local para interpretar el reporte
7. Guarda la interpretación en un archivo de texto

![Vista de la aplicación](img/captura.png)
---

## Qué NO hace este proyecto

- No limpia datos
- No modifica el dataset original
- No entrena modelos de machine learning
- No utiliza servicios en la nube
- No envía datos a plataformas externas

El foco está en **proceso, criterio y buenas prácticas**, no en automatización total.

---

## Uso responsable de IA

La IA utilizada en este proyecto:

- se ejecuta completamente en entorno local
- no tiene acceso al dataset original
- recibe únicamente un reporte resumido
- no toma decisiones finales
- no realiza cálculos

Su rol es **interpretar resultados**, no analizar datos crudos.

---

## Seguridad y privacidad

Todo el flujo de trabajo se ejecuta localmente en la computadora del usuario:

- los datos no salen del entorno local
- no se utilizan APIs externas
- no se requiere conexión a internet
- no se sube información a servicios de terceros

Este enfoque es adecuado para trabajar con datos sensibles o confidenciales.

---

## Estructura del proyecto
```
dataset_validator/
│
├── data/
│ └── adult.csv
│
├── src/
│ ├── inspect_data.py
│ └── interpretar_reporte.py
│
├── reporte_validacion.json
├── interpretacion_reporte.txt
└── README.md
```

---

## Modelos de IA local recomendados (según recursos)

Este proyecto no depende de un modelo específico.  
Cualquier modelo de lenguaje que pueda ejecutarse localmente y responder a prompts en español es suficiente para cumplir el objetivo pedagógico.

Se priorizan modelos livianos, accesibles y reproducibles, ya que la IA solo interpreta un reporte resumido y no procesa datos crudos.

### Opciones recomendadas (ordenadas por menor consumo de recursos)

#### Modelos muy livianos (CPU / baja RAM)

Adecuados para notebooks sin GPU o equipos con recursos limitados:

- phi-2  
- tinyllama  
- qwen2.5-1.5b  
- mistral-7b-instruct (versiones cuantizadas)

Estos modelos ofrecen velocidad moderada y calidad suficiente para tareas de interpretación simple.

---

####  Modelos intermedios (CPU potente o GPU básica)

Buen equilibrio entre calidad de salida y consumo de recursos:

- nous-hermes-2-mistral-7b-dpo (utilizado en este ejemplo)
- openhermes-2.5-mistral  
- qwen2.5-7b-instruct  

Recomendados para una experiencia más fluida sin requerir hardware avanzado.

---

#### Modelos de mayor tamaño (opcional)

No son necesarios para este ejemplo, aunque pueden utilizarse:

- Modelos de 13B o superiores  

Requieren mayor capacidad de cómputo y no aportan valor pedagógico adicional para este pipeline.

---

## Requisitos

Para ejecutar el flujo completo del repositorio:

### Parte Python
- Python 3.10 o superior  
- Funciona en cualquier equipo estándar

### Parte IA local (LM Studio)
Los requerimientos dependen del modelo elegido:

- CPU: suficiente para modelos livianos  
- RAM: desde 8 GB (modelos pequeños)  
- GPU: opcional, mejora los tiempos de respuesta  
- Conexión a internet: no requerida para la ejecución

El proyecto está diseñado para adaptarse al hardware disponible y no exige infraestructura especializada.

No se requieren cuentas, pagos ni servicios externos.

---

## Qué se espera aprender con este proyecto

Al finalizar este ejercicio, el estudiante debería ser capaz de:

- comprender la importancia de la validación inicial de datos
- aplicar reglas automáticas simples con criterio
- separar lógica de interpretación
- integrar IA de manera justificada y controlada
- pensar en términos de procesos reutilizables

---

## Público objetivo

Este proyecto está pensado para estudiantes de análisis de datos con nivel intermedio que deseen dar el primer paso hacia flujos de trabajo más estructurados sin introducir complejidad innecesaria.

Se priorizan criterios pedagógicos, accesibilidad y reproducibilidad.

Existen múltiples formas de enriquecer o sofisticar el pipeline (otras herramientas, servicios pagos, arquitecturas más complejas, optimizaciones adicionales, etc.).

Aquí se eligió deliberadamente un enfoque simple, local y abierto, pensado para facilitar el aprendizaje, la comprensión de los conceptos y la experimentación por parte de personas que están incorporando estas herramientas.

El objetivo no es mostrar “la mejor” solución posible, sino una solución clara, explicable y transferible.

---

## Dataset

El dataset utilizado en este proyecto es **Adult Income Dataset**, disponible públicamente en Kaggle:

https://www.kaggle.com/datasets/wenruliu/adult-income-dataset

### Descripción

Este conjunto de datos contiene información demográfica y laboral de personas adultas.

Incluye variables como:
- Edad
- Nivel educativo
- Estado civil
- Tipo de trabajo
- Ocupación
- Horas trabajadas por semana
- País de origen
- Ingreso (variable objetivo)

El dataset es ampliamente utilizado con fines educativos para prácticas de:
- Análisis exploratorio de datos (EDA)
- Limpieza y validación de datos
- Preparación de datasets para modelos de machine learning
- Discusión sobre sesgos y calidad de datos

### Licencia y uso

El dataset es de acceso público y se utiliza en este proyecto **exclusivamente con fines educativos**.
No contiene información personal identificable y no se incorporan datos sensibles adicionales durante el procesamiento.

---

### Autoría y Contacto

**Regina N. Molares**
*Analista Técnico Funcional | Especialista en Datos y Educación*

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Regina_Molares-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/regina-molares) 

  
[![Notion](https://img.shields.io/badge/Portafolio-Ver_en_Notion-000000?style=for-the-badge&logo=notion&logoColor=white)](https://www.notion.so/Portfolio-DATA-REGINA-Regina-N-Molares-285b0a3d6be08016ab11e0359468c52e?source=copy_link)
  

*© 2025-2026. La estructura analítica y metodológica de este documento pertenecen a su autora.*



