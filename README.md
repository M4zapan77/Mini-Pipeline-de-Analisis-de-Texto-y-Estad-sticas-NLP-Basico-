# Mini-Pipeline de Análisis de Texto y Estadísticas

**Proyecto Final — Programación I en Python**

**Universidad Iberoamericana León**  
**Docente:** Mtro. Edgar Arenas  
**Lenguaje:** Python 3

## Descripción

Aplicación desarrollada en Python para realizar análisis estadístico y procesamiento básico de lenguaje natural (NLP). Permite analizar textos, identificar palabras frecuentes y clasificar sentimientos mediante un diccionario de polaridad.

El proyecto utiliza una arquitectura modular e incorpora una interfaz gráfica con Tkinter y soporte para diferentes formatos de documentos.

## Funcionalidades

### Estadísticas básicas
- Conteo de palabras, caracteres y oraciones.
- Longitud promedio de palabras y oraciones.

### Procesamiento de Lenguaje Natural (NLP)
- Limpieza y tokenización de texto.
- Filtrado de *stop words* mediante conjuntos.
- Cálculo de diversidad léxica (TTR).
- Identificación de las 5 palabras más frecuentes.

### Análisis de sentimientos
- Diccionario de palabras positivas y negativas.
- Cálculo de puntuación acumulada.
- Clasificación: positivo, negativo o neutro.

### Lectura de archivos e interfaz
- Importación de archivos TXT, PDF, DOCX y Markdown.
- Entrada manual de texto.
- Visualización de resultados mediante Tkinter.

## Estructura del proyecto

```text
proyecto_py/
├── main.py
├── README.md
├── analizador/
│   ├── __init__.py
│   ├── archivos.py
│   ├── estadisticas.py
│   ├── interfaz.py
│   ├── nlp.py
│   └── sentimientos.py
└── empaquetado/
    └── AnalizadorNLP.spec
```

Cada módulo tiene una responsabilidad específica. `main.py` es el punto de entrada y debe contener un máximo de 20 líneas.

## Instalación y ejecución

Desde la raíz del proyecto, ejecuta el programa con Python 3 y Tkinter.

```bash
python main.py
```

### Generar ejecutable para Windows

```bash
python -m pip install pyinstaller
python -m PyInstaller empaquetado/AnalizadorNLP.spec
```

El ejecutable se genera en `dist/AnalizadorNLP.exe`.

## Tecnologías

- Python 3
- Tkinter
- pypdf
- python-docx
- Git y GitHub
- PyInstaller


**Diego Isaac Rico Hernández** 

**Mariano Hernández Antuñano**


Ingeniería en Inteligencia Artificial  
Universidad Iberoamericana León

**Fecha de entrega:** 1 de diciembre de 2026.
