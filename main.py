from archivos import texto
from Estadistica_Basica import analizar_estadisticas
from UI import abrir_ventana

def main():
    resultados = analizar_estadisticas(texto())
    for nombre, valor in resultados.items():
        print(f"{nombre}: {valor}")
    abrir_ventana()

if __name__ == "__main__":
    main()