# Cambiar esta línea:
# from src.lab05.csv_xlsx import csv_to_xlsx

# Por esta (importación relativa):
from .csv_xlsx import csv_to_xlsx

try:
    csv_to_xlsx("../data/samples/people.csv", "../data/out/people.xlsx")
    print("✅ ¡CSV convertido a XLSX exitosamente!")
except Exception as e:
    print(f"❌ Error: {e}")