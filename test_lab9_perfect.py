import sys
import os
sys.path.insert(0, os.path.join(os.getcwd(), 'src'))

print("=== LAB 9 - VERSIÓN FINAL ===")

try:
    from lab09 import Group, Student
    print("✅ Módulos importados correctamente")
    
    # 1. Crear grupo
    csv_file = "data/lab09/final_students.csv"
    group = Group(csv_file)
    print(f"✅ Grupo inicializado. Archivo: {csv_file}")
    
    # 2. Añadir estudiantes (usando full_name en vez de fio)
    students_data = [
        {"full_name": "Иванов Иван Иванович", "birthdate": "2003-10-10", "group": "БИВТ-21-1", "gpa": 4.3},
        {"full_name": "Петров Петр Петрович", "birthdate": "2002-05-15", "group": "БИВТ-21-2", "gpa": 3.8},
        {"full_name": "Сидорова Анна", "birthdate": "2003-02-20", "group": "БИВТ-21-1", "gpa": 4.7},
        {"full_name": "Кузнецов Алексей", "birthdate": "2002-11-30", "group": "БИВТ-21-3", "gpa": 3.5},
        {"full_name": "Смирнова Мария", "birthdate": "2003-07-22", "group": "БИВТ-21-2", "gpa": 4.9},
    ]
    
    print("\n➕ Añadiendo estudiantes...")
    for data in students_data:
        student = Student(
            full_name=data["full_name"],
            birthdate=data["birthdate"],
            group=data["group"],
            gpa=data["gpa"]
        )
        group.add(student)
        print(f"   ✅ {data['full_name']}")
    
    # 3. Listar todos los estudiantes
    print("\n📋 LISTA COMPLETA DE ESTUDIANTES:")
    all_students = group.list()
    for i, student in enumerate(all_students, 1):
        print(f"{i:2}. {student.full_name:25} | {student.group:12} | {student.gpa} | {student.birthdate}")
    
    # 4. Buscar estudiantes
    print("\n🔍 BUSQUEDA (por 'Иванов'):")
    found_students = group.find("Иванов")
    for student in found_students:
        print(f"   • {student.full_name} - {student.group} - GPA: {student.gpa}")
    
    # 5. Actualizar estudiante
    print("\n✏️  ACTUALIZANDO GPA de Иванов...")
    if group.update("Иванов Иван Иванович", gpa=4.8):
        print("   ✅ GPA actualizado a 4.8")
    
    # 6. Estadísticas
    print("\n📊 ESTADÍSTICAS DEL GRUPO:")
    stats = group.stats()
    print(f"   • Total estudiantes: {stats['count']}")
    print(f"   • GPA mínimo: {stats['min_gpa']}")
    print(f"   • GPA máximo: {stats['max_gpa']}")
    print(f"   • GPA promedio: {stats['avg_gpa']:.2f}")
    print(f"   • Distribución por grupos: {stats['groups']}")
    
    print("\n🏆 TOP 5 ESTUDIANTES:")
    for i, top in enumerate(stats['top_5_students'], 1):
        print(f"   {i}. {top['full_name']} - GPA: {top['gpa']}")
    
    # 7. Eliminar un estudiante
    print("\n🗑️  ELIMINANDO estudiante...")
    if group.remove("Петров Петр Петрович"):
        print("   ✅ Петров Петр Петрович eliminado")
    
    # 8. Verificación final
    print("\n✅ VERIFICACIÓN FINAL:")
    final_students = group.list()
    print(f"   Total final: {len(final_students)} estudiantes")
    
    # 9. Ver archivo CSV
    print("\n💾 ARCHIVO CSV GENERADO:")
    if os.path.exists(csv_file):
        print(f"   📂 {csv_file}")
        print("   Contenido:")
        print("-" * 60)
        with open(csv_file, 'r', encoding='utf-8') as f:
            print(f.read())
        print("-" * 60)
    else:
        print("   ❌ Archivo no encontrado")
    
    print("\n" + "="*60)
    print("🎉 ¡LABORATORIO 9 COMPLETADO EXITOSAMENTE!")
    print("="*60)
    
except ImportError as e:
    print(f"❌ Error de importación: {e}")
    print("\nPosible solución:")
    print("1. Asegúrate de que lab08 esté completado")
    print("2. Verifica que src/lab09/__init__.py existe")
    
except Exception as e:
    print(f"\n❌ ERROR: {type(e).__name__}")
    print(f"Mensaje: {e}")
    import traceback
    traceback.print_exc()
