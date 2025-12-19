# src/lab09/group.py
import csv
from pathlib import Path
from typing import List
import sys
import os

# Añadir para poder importar Student del Lab 8
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from lab08.models import Student


class Group:
    """Clase para manejar una 'base de datos' de estudiantes en CSV"""
    
    def __init__(self, storage_path: str):
        """
        Inicializa el grupo con un archivo CSV
        storage_path: ruta al archivo CSV (ej: 'data/lab09/students.csv')
        """
        self.path = Path(storage_path)
        self._ensure_storage_exists()
    
    def _ensure_storage_exists(self):
        """Crea el archivo CSV con encabezados si no existe"""
        if not self.path.exists():
            # Crear directorio si no existe
            self.path.parent.mkdir(parents=True, exist_ok=True)
            # Crear archivo con encabezados
            with open(self.path, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['full_name', 'birthdate', 'group', 'gpa'])
            print(f"✓ Archivo CSV creado: {self.path}")
    
    def _read_all_rows(self) -> List[dict]:
        """Lee todas las filas del CSV (interno)"""
        rows = []
        if self.path.exists():
            with open(self.path, 'r', newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    rows.append(row)
        return rows
    
    def _write_all_rows(self, rows: List[dict]):
        """Escribe todas las filas al CSV (interno)"""
        with open(self.path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['full_name', 'birthdate', 'group', 'gpa'])
            writer.writeheader()
            writer.writerows(rows)
    
    def list(self) -> List[Student]:
        """Obtener todos los estudiantes"""
        rows = self._read_all_rows()
        students = []
        
        for row in rows:
            try:
                student = Student(
                    full_name=row['full_name'],
                    birthdate=row['birthdate'],
                    group=row['group'],
                    gpa=float(row['gpa'])
                )
                students.append(student)
            except Exception as e:
                print(f"Error al crear estudiante {row}: {e}")
        
        return students
    
    def add(self, student: Student):
        """Agregar un nuevo estudiante"""
        rows = self._read_all_rows()
        
        # Verificar si ya existe
        for row in rows:
            if row['full_name'] == student.full_name:
                print(f" Estudiante {student.full_name} ya existe")
                return False
        
        # Agregar nuevo
        rows.append({
            'full_name': student.full_name,
            'birthdate': student.birthdate,
            'group': student.group,
            'gpa': str(student.gpa)
        })
        
        self._write_all_rows(rows)
        print(f"✓ Estudiante {student.full_name} agregado")
        return True
    
    def find(self, substr: str) -> List[Student]:
        """Buscar estudiantes por texto en el nombre"""
        all_students = self.list()
        found = []
        
        for student in all_students:
            if substr.lower() in student.full_name.lower():
                found.append(student)
        
        return found
    
    def remove(self, full_name: str) -> bool:
        """Eliminar un estudiante por nombre completo"""
        rows = self._read_all_rows()
        original_count = len(rows)
        
        # Filtrar (eliminar) el estudiante
        rows = [row for row in rows if row['full_name'] != full_name]
        
        if len(rows) < original_count:
            self._write_all_rows(rows)
            print(f"studiante {full_name} eliminado")
            return True
        else:
            print(f" Estudiante {full_name} no encontrado")
            return False
    
    def update(self, full_name: str, **fields) -> bool:
        """Actualizar campos de un estudiante"""
        rows = self._read_all_rows()
        updated = False
        
        for row in rows:
            if row['full_name'] == full_name:
                # Actualizar campos permitidos
                if 'full_name' in fields:
                    row['full_name'] = fields['full_name']
                if 'birthdate' in fields:
                    row['birthdate'] = fields['birthdate']
                if 'group' in fields:
                    row['group'] = fields['group']
                if 'gpa' in fields:
                    row['gpa'] = str(fields['gpa'])
                
                updated = True
                break
        
        if updated:
            self._write_all_rows(rows)
            print(f" Estudiante {full_name} actualizado")
            return True
        else:
            print(f" Estudiante {full_name} no encontrado")
            return False
    
    def stats(self) -> dict:
        """Estadísticas del grupo (extra)"""
        students = self.list()
        
        if not students:
            return {
                "count": 0,
                "min_gpa": 0,
                "max_gpa": 0,
                "avg_gpa": 0,
                "groups": {},
                "top_5_students": []
            }
        
        # Calcular GPA
        gpas = [s.gpa for s in students]
        
        # Contar por grupo
        groups_count = {}
        for student in students:
            group = student.group
            groups_count[group] = groups_count.get(group, 0) + 1
        
        # Top 5 estudiantes por GPA
        sorted_students = sorted(students, key=lambda s: s.gpa, reverse=True)
        top_5 = [
            {"full_name": s.full_name, "gpa": s.gpa}
            for s in sorted_students[:5]
        ]
        
        return {
            "count": len(students),
            "min_gpa": min(gpas),
            "max_gpa": max(gpas),
            "avg_gpa": sum(gpas) / len(gpas),
            "groups": groups_count,
            "top_5_students": top_5
        }


# Ejemplo de uso
if __name__ == "__main__":
    print("=== DEMO: Clase Group ===")
    
    # Crear grupo (base de datos)
    grupo = Group("data/lab09/students.csv")
    
    # Agregar algunos estudiantes
    estudiante1 = Student(
        full_name="Ivanov Ivan Ivanovich",
        birthdate="2000-05-15",
        group="SE-001",
        gpa=4.5
    )
    
    estudiante2 = Student(
        full_name="Petrova Maria Sergeevna",
        birthdate="2001-11-23",
        group="SE-002",
        gpa=4.8
    )
    
    print("\n1. Agregando estudiantes...")
    grupo.add(estudiante1)
    grupo.add(estudiante2)
    
    print("\n2. Listando todos...")
    todos = grupo.list()
    for i, estudiante in enumerate(todos, 1):
        print(f"{i}. {estudiante}")
    
    print("\n3. Buscando 'Ivan'...")
    encontrados = grupo.find("Ivan")
    for estudiante in encontrados:
        print(f" {estudiante}")
    
    print("\n4. Estadísticas...")
    estadisticas = grupo.stats()
    print(f"Total: {estadisticas['count']} estudiantes")
    print(f"GPA promedio: {estadisticas['avg_gpa']:.2f}")
    print(f"Grupos: {estadisticas['groups']}")