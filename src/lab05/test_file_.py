import sys
import os

# Agregar el directorio actual al path
sys.path.insert(0, os.getcwd())

try:
    from src.lab05.csv_xlsx import csv_to_xlsx
    print("✅ Módulo importado correctamente!")
    
    # Probar la función
    csv_to_xlsx("data/samples/people.csv", "data/out/people.xlsx")
    print("✅ CSV → XLSX: CONVERSIÓN EXITOSA!")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()