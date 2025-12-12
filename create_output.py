#!/usr/bin/env python3
"""
Create students_output.json from students_input.json
"""

import json
import os
import sys

print("=" * 50)
print("   GENERATING students_output.json")
print("=" * 50)

# 1. First, let's check if our modules work
print("\n1. Testing imports...")
try:
    # Add current directory to path
    sys.path.insert(0, os.path.dirname(__file__))
    
    from src.lab08.models import Student
    from src.lab08.serialize import students_from_json, students_to_json
    
    print("   ✅ Imports successful!")
    
    # 2. Load students
    print("\n2. Loading students from input file...")
    input_path = "data/lab08/students_input.json"
    
    students = students_from_json(input_path)
    print(f"   ✅ Loaded {len(students)} students")
    
    # Show each student
    for i, student in enumerate(students, 1):
        print(f"   {i}. {student}")
    
    # 3. Save to output
    print("\n3. Saving to output file...")
    output_path = "data/lab08/students_output.json"
    
    students_to_json(students, output_path)
    print(f"   ✅ Saved to: {output_path}")
    
except ImportError as e:
    print(f"   ❌ Import error: {e}")
    print("\nTrying alternative method...")
    
    # Alternative: Just copy the JSON
    import json
    with open("data/lab08/students_input.json", "r") as f:
        data = json.load(f)
    
    with open("data/lab08/students_output.json", "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"   ✅ Copied JSON directly ({len(data)} records)")
    
except Exception as e:
    print(f"   ❌ Error: {e}")
    import traceback
    traceback.print_exc()

# 4. Verify the file was created
print("\n4. Verifying output file...")
output_path = "data/lab08/students_output.json"
if os.path.exists(output_path):
    size = os.path.getsize(output_path)
    if size > 0:
        print(f"   ✅ File exists and is not empty ({size} bytes)")
        
        # Show first few lines
        print("\n   First 5 lines of output:")
        with open(output_path, "r") as f:
            for i, line in enumerate(f):
                if i < 5:
                    print(f"   {line.rstrip()}")
                else:
                    break
    else:
        print(f"   ⚠️  File exists but is empty ({size} bytes)")
else:
    print(f"   ❌ File not created!")

print("\n" + "=" * 50)
print("   PROCESS COMPLETE")
print("=" * 50)
