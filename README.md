Proyecto: Análisis de Ventas por Provincia

Autor: Edison Vela
Curso: Taller de Programación / Práctica 03

📌 Descripción del Proyecto

Este proyecto implementa un analizador de datos de ventas utilizando Python.
El sistema permite:

Cargar información desde un archivo CSV grande (≈ 49.000 filas)

Limpiar y normalizar datos

Calcular ventas totales por provincia

Buscar ventas específicas de una provincia

Manejar errores cuando la provincia no existe

Validar funcionalidades con pruebas unitarias (unittest)

Medir la cobertura del código con coverage, incluyendo un reporte HTML

El objetivo principal es aplicar buenas prácticas de programación, testing y documentación.

🧠 Estructura del Proyecto
practica-03/
│── src/
│    └── procesador.py        # Lógica principal del analizador
│
│── tests/
│    └── test_analizador.py   # Pruebas unitarias
│       └── test_procesador.py
│── data/
│    └── ventas.csv           # Archivo con 49852 registros
│
│── htmlcov/                  # Reporte coverage HTML (generado)
│──.gitignore
│──app.py
│── README.md
│── requirements.txt

🐍 Funcionalidades Principales
✔ Carga y limpieza de datos

El sistema normaliza nombres de provincia, convierte tipos y elimina filas inválidas.

✔ Ventas totales por provincia
analizador.ventas_totales_por_provincia()


Devuelve un diccionario con todas las provincias y su total de ventas.

✔ Búsqueda de una provincia específica
analizador.ventas_por_provincia("PICHINCHA")

✔ Manejo de errores

Si una provincia no existe, se lanza:

ValueError("Provincia no encontrada: <nombre>")

🧪 Ejecución de Pruebas Unitarias

Ejecutar todas las pruebas:

python -m unittest discover tests


Resultado esperado:

Ran 6 tests in ...
OK

📈 Generación de Coverage

1️⃣ Ejecutar cobertura:

coverage run -m unittest discover tests


2️⃣ Mostrar reporte en consola:

coverage report


3️⃣ Generar el reporte HTML:

coverage html


Esto creará una carpeta llamada htmlcov/ con un archivo:

htmlcov/index.html


Puedes abrirlo en VS Code o navegador para ver la cobertura visual.

🔍 Resultados del Proyecto

6 pruebas unitarias exitosas

Cobertura generada correctamente

Validación de casos normales + excepciones

Análisis eficiente de archivo grande (≈50k filas)

Código limpio y organizado

📚 Tecnologías Usadas

Python 3

unittest

coverage

CSV / manipulación de datos

VS Code / PowerShell

👤 Autor

Edison Vela
Estudiante de Negocios Digitales
Apasionado por programación, análisis de datos y VR