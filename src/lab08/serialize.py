#!/usr/bin/env python3
import json
from datetime import datetime
from .models import Student

def load_students(filepath):
    """Load students from JSON file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    students = []
    for item in data:
        try:
            student = Student(
                full_name=item['full_name'],
                birthdate=item['birthdate'],
                group=item['group'],
                gpa=item['gpa']
            )
            students.append(student)
        except Exception as e:
            print(f"Error creating student: {e}")
    
    return students

def save_students(students, filepath):
    """Save students to JSON file"""
    data = []
    for student in students:
        data.append(student.to_dict())
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"JSON file saved: {filepath}")

def main():
    """Main function to run the serialization"""
    input_file = "../../data/lab08/students_input.json"
    output_file = "../../data/lab08/students_output.json"
    
    print("Loading students from input file...")
    students = load_students(input_file)
    print(f"Loaded {len(students)} students")
    
    for i, student in enumerate(students, 1):
        print(f"{i}. {student}")
    
    print("\nSaving to output file...")
    save_students(students, output_file)
    print(f"Saved to: {output_file}")

if __name__ == "__main__":
    main()
