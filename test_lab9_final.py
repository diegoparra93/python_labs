import sys
import os

# Configurar path
sys.path.insert(0, os.path.join(os.getcwd(), 'src'))

print("=== TEST LAB 9 ===")
print("Path:", sys.path)

try:
    from lab09 import Group, Student
    print("✅ Import exitoso")
    
    # 1. Crear grupo
    csv_path = "data/lab09/students_lab9.csv"
    group = Group(csv_path)
    print(f"✅ Grupo creado. Archivo: {csv_path}")
    
    # 2. Añadir estudiantes de prueba
    estudiantes = [
        ("Ivanov Ivan Ivanovich", "2003-10-10", "БИВТ-21-1", 4.3),
        ("Petrov Petr Petrovich", "2002-05-15", "БИВТ-21-2", 3.8),
        ("Sidorova Anna", "2003-02-20", "БИВТ-21-1", 4.7),
    ]
    
    for fio, fecha, grupo, gpa in estudiantes:
        student = Student(fio, fecha, grupo, gpa)
        group.add(student)
        print(f"  ✅ Añadido: {fio}")
    
    # 3. Mostrar todos
    print("\n📋 Lista completa:")
    all_students = group.list()
    for i, s in enumerate(all_students, 1):
        print(f"  {i}. {s.fio:25} | {s.group:12} | GPA: {s.gpa}")
    
    # 4. Buscar
    print("\n🔍 Buscando 'Ivan':")
    found = group.find("Ivan")
    for s in found:
        print(f"  Encontrado: {s.fio}")
    
    # 5. Estadísticas
    print("\n📊 Estadísticas:")
    stats = group.stats()
    print(f"  Total: {stats['count']} estudiantes")
    print(f"  GPA promedio: {stats['avg_gpa']:.2f}")
    print(f"  GPA mínimo: {stats['min_gpa']}")
    print(f"  GPA máximo: {stats['max_gpa']}")
    
    # 6. Verificar archivo
    if os.path.exists(csv_path):
        print(f"\n✅ Archivo CSV creado: {csv_path}")
        with open(csv_path, 'r') as f:
            lines = f.readlines()
            print(f"  Tiene {len(lines)} líneas")
    else:
        print(f"\n❌ Archivo no creado")
    
    print("\n🎉 ¡LAB 9 COMPLETADO EXITOSAMENTE!")
    
except Exception as e:
    print(f"\n❌ ERROR: {type(e).__name__}")
    print(f"Mensaje: {e}")
    import traceback
    traceback.print_exc()
