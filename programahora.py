# Importem el mòdul datetime
import datetime

# Mostrar la data i hora actual formatada
data_actual = datetime.datetime.now()
data_formatada = data_actual.strftime("%d/%m/%Y %H:%M")
print(f"Data i hora actual: {data_formatada}")

# Calcular quants dies falten per una data concreta (ex. Nadal)
data_nadal = datetime.datetime(data_actual.year, 12, 25)  # Nadal és el 25 de desembre

# Si Nadal ja ha passat aquest any, calculem per l'any següent
if data_actual > data_nadal:
    data_nadal = datetime.datetime(data_actual.year + 1, 12, 25)

# Calcular la diferència en dies
dies_falten = (data_nadal - data_actual).days
print(f"Queden {dies_falten} dies per Nadal.")
