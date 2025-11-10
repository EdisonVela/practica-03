import csv
class Analizador:
    def __init__(self, ruta_csv):
        self.ruta_csv = ruta_csv
        try:
            self.datos = self._leer_csv()
            print(f"DEBUG: {len(self.datos)} filas cargadas correctamente.")
        except Exception as e:
            print(f"ERROR al inicializar el analizador: {e}")
            self.datos = []

    def _leer_csv(self):
        """Lee el archivo CSV y devuelve una lista de diccionarios. Usa '|' como delimitador."""
        datos = []
        try:
            with open(self.ruta_csv, "r", encoding="utf-8") as archivo:
                lector = csv.DictReader(archivo, delimiter='|')
                for fila in lector:
                    datos.append(fila)
        except FileNotFoundError:
            print(f"ERROR: No se encontró el archivo: {self.ruta_csv}")
            return []
        except Exception as e:
            raise e
        return datos
    def ventas_totales_por_provincia(self):
        """Devuelve un diccionario con el total de ventas por provincia."""
        totales = {}

        for fila in self.datos:
            try:
                provincia = fila["PROVINCIA"]
                total_venta = float(fila["TOTAL_VENTAS"])

                if provincia not in totales:
                    totales[provincia] = total_venta
                else:
                    totales[provincia] += total_venta
            except KeyError:
                print("ADVERTENCIA: Faltan columnas en una fila y fue omitida.")
                continue
            except ValueError:
                print("ADVERTENCIA: 'TOTAL_VENTAS' no es un número y fue omitido.")
                continue

        return totales

    def ventas_por_provincia(self, nombre):
        """Devuelve el total de ventas de una provincia específica."""
        totales = self.ventas_totales_por_provincia()

        if nombre in totales:
            return totales[nombre]
        else:
            return 0.0 