"""Estadisticas Basicas y Estructurales: Conteo total de palabras, conteo de caracteres,
conteo total de oraciones, longitud promedio de palabras y de oraciones.
"""
from archivos import texto

def limpiar_palabra(palabra):
    puntuacion = ".,;:!?¡¿()[]{}\"'"
    return palabra.strip(puntuacion)

def contar_palabras(texto):
    palabras = texto.split()
    return len([palabra for palabra in palabras if limpiar_palabra(palabra)])

def contar_caracteres(texto):
    caracteres_con_espacios = len(texto)
    caracteres_sin_espacios = 0
    for caracter in texto:
        if not caracter.isspace():
            caracteres_sin_espacios += 1
    return caracteres_con_espacios, caracteres_sin_espacios

def obtener_oraciones(texto):
    oraciones = []
    oracion_actual = ""
    for caracter in texto:
        oracion_actual += caracter
        if caracter in ".!?":
            if contar_palabras(oracion_actual) > 0:
                oraciones.append(oracion_actual.strip())
            oracion_actual = ""
    if contar_palabras(oracion_actual) > 0:
        oraciones.append(oracion_actual.strip())
    return oraciones

def contar_oraciones(texto):
    return len(obtener_oraciones(texto))

def longitud_promedio_palabras(texto):
    palabras = texto.split()
    total_caracteres = 0
    total_palabras = 0
    for palabra in palabras:
        palabra_limpia = limpiar_palabra(palabra)
        if palabra_limpia:
            total_caracteres += len(palabra_limpia)
            total_palabras += 1
    if total_palabras == 0:
        return 0
    return total_caracteres / total_palabras

def longitud_promedio_oraciones(texto):
    oraciones = obtener_oraciones(texto)
    if not oraciones:
        return 0
    total_palabras = 0
    for oracion in oraciones:
        total_palabras += contar_palabras(oracion)
    return total_palabras / len(oraciones)

def analizar_estadisticas(texto):
    caracteres_con, caracteres_sin = contar_caracteres(texto)
    return {
        "Total de palabras": contar_palabras(texto),
        "Caracteres con espacios": caracteres_con,
        "Caracteres sin espacios": caracteres_sin,
        "Total de oraciones": contar_oraciones(texto),
        "Longitud promedio de palabras": round(longitud_promedio_palabras(texto), 2),
        "Longitud promedio de oraciones": round(longitud_promedio_oraciones(texto), 2)
    }

##prueba de salida de texto 
resultados = analizar_estadisticas(texto())
for nombre, valor in resultados.items():
    print(nombre, ":", valor)
    