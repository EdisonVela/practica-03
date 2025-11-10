from src.procesador import Analizador

def main():
    archivo = "datos/sri_ventas_2024.csv"
    analizador = Analizador(archivo)
    if not analizador.datos:
        print(f"ERROR: No se pudo continuar el análisis. Verifique el archivo y la ruta: {archivo}")
        return
    print("Ventas totales por provincia:")
    resumen = analizador.ventas_totales_por_provincia()
    
    for prov, total in resumen.items():
        print(f"\t{prov}: ${total:,.2f}") 
    print("\nCompras para una provincia")
    provincia = input("\tIngrese el nombre de una provincia: ")
    
    ventas = analizador.ventas_por_provincia(provincia)
    if ventas > 0.0:
        print(f"\tVentas de {provincia}: ${ventas:,.2f}")
    else:
        print(f"\tERROR: No se encontraron ventas para la provincia '{provincia}'.")
if __name__ == "__main__":
    main()