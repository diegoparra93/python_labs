import sys

sys.path.append(".")

from src.lab05.csv_xlsx import csv_to_xlsx

try:
    print("🔍 Depurando csv_to_xlsx...")

    # Verificar archivo de entrada
    with open("data/samples/people.csv", "r", encoding="utf-8") as f:
        content = f.read()
        print(f"📄 Contenido del CSV: {len(content)} caracteres")
        print("Primeras líneas:")
        print(content[:200])

    # Ejecutar la función
    csv_to_xlsx("data/samples/people.csv", "data/out/people_debug.xlsx")
    print("✅ Función ejecutada sin errores")

except Exception as e:
    print(f"❌ Error: {e}")
    import traceback

    traceback.print_exc()
