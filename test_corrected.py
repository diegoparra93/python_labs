import sys
import os
sys.path.insert(0, os.path.join(os.getcwd(), 'src'))

print("=== TEST LAB 9 - CORREGIDO ===")

try:
    from lab09 import Group, Student
    print("✅ Import exitoso")
    
    # Crear grupo
    group = Group("data/lab09/students_final.csv")
    print("✅ Grupo creado")
    
    # Crear estudiante de prueba
    test_student = Student("Test Name", "2000-01-01", "TEST-01", 4.0)
    print("✅ Estudiante creado")
    
    # VER QUÉ ATRIBUTOS TIENE REALMENTE
    print("\n🔍 Atributos del estudiante:")
    print(f"  Dirección: {dir(test_student)}")
    print(f"  Tipo: {type(test_student)}")
    
    # Intentar acceder a diferentes nombres posibles
    attrs_to_try = ['fio', 'name', 'full_name', 'nombre', '__dict__']
    for attr in attrs_to_try:
        if hasattr(test_student, attr):
            print(f"  ✅ Tiene '{attr}': {getattr(test_student, attr)}")
    
    # Mostrar todos los atributos
    print("\n📦 Todos los atributos (__dict__):")
    if hasattr(test_student, '__dict__'):
        for key, value in test_student.__dict__.items():
            print(f"  {key}: {value}")
    
    print("\n🎉 Debug completado")
    
except Exception as e:
    print(f"\n❌ ERROR: {type(e).__name__}: {e}")
