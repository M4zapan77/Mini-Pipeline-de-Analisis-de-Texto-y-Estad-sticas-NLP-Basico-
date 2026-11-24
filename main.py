from analizador.archivos import texto
from analizador.estadisticas import analizar_estadisticas
from analizador.interfaz import abrir_ventana

def main():
    resultados = analizar_estadisticas(texto())
    for nombre, valor in resultados.items():
        print(f"{nombre}: {valor}")
    abrir_ventana()

if __name__ == "__main__":
    main()