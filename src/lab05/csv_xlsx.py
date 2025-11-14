import csv
from pathlib import Path
from openpyxl import Workbook
from openpyxl.utils import get_column_letter

def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """
    Convierte CSV a XLSX usando openpyxl
    """
    print(f"🔍 Iniciando conversión: {csv_path} → {xlsx_path}")
    
    # Validar que el archivo existe
    csv_file = Path(csv_path)
    if not csv_file.exists():
        raise FileNotFoundError(f"Archivo CSV no encontrado: {csv_path}")
    
    # Leer CSV
    with open(csv_path, 'r', encoding='utf-8') as cf:
        reader = csv.reader(cf)
        rows = list(reader)
    
    print(f"📊 Filas leídas del CSV: {len(rows)}")
    
    if not rows:
        raise ValueError("El archivo CSV está vacío")
    
    # Mostrar contenido para debug
    for i, row in enumerate(rows):
        print(f"  Fila {i}: {row}")
    
    # Crear workbook y worksheet
    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"
    
    # Escribir datos
    for row in rows:
        ws.append(row)
    
    print("📝 Datos escritos en XLSX")
    
    # Ajustar auto-ancho de columnas
    for col_idx, column in enumerate(ws.columns, 1):
        max_length = 0
        column_letter = get_column_letter(col_idx)
        
        for cell in column:
            try:
                if cell.value and len(str(cell.value)) > max_length:
                    max_length = len(str(cell.value))
            except:
                pass
        
        adjusted_width = max(max_length + 2, 8)
        ws.column_dimensions[column_letter].width = adjusted_width
        print(f"  📏 Columna {column_letter}: ancho {adjusted_width}")
    
    # Crear directorio si no existe
    Path(xlsx_path).parent.mkdir(parents=True, exist_ok=True)
    
    # Guardar archivo (¡ESTA ES LA PARTE IMPORTANTE!)
    wb.save(xlsx_path)
    print(f"💾 XLSX guardado exitosamente: {xlsx_path}")
    
    # Verificar que se creó
    if Path(xlsx_path).exists():
        file_size = Path(xlsx_path).stat().st_size
        print(f"📁 Tamaño del archivo: {file_size} bytes")
    else:
        print("❌ ERROR: El archivo XLSX no se creó")