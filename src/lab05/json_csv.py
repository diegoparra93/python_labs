import csv
import json
from pathlib import Path

def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Converts CSV to JSON (list of dictionaries)
    """
    csv_file = Path(csv_path)
    json_file = Path(json_path)
    
    # Check if CSV exists
    if not csv_file.exists():
        raise FileNotFoundError(f"CSV file not found: {csv_path}")
    
    # Read CSV and convert to JSON
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        data = list(reader)
    
    if not data:
        raise ValueError("CSV file is empty")
    
    # Create output directory
    json_file.parent.mkdir(parents=True, exist_ok=True)
    
    # Write JSON file
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Converts JSON to CSV (list of dictionaries to CSV)
    """
    json_file = Path(json_path)
    csv_file = Path(csv_path)
    
    # Check if JSON file exists
    if not json_file.exists():
        raise FileNotFoundError(f"JSON file not found: {json_path}")
    
    # Read JSON
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Validate JSON structure
    if not isinstance(data, list):
        raise ValueError("It must contain a dictionary list")
    
    if not data:
        raise ValueError("JSON file is empty")
    
    if not all(isinstance(item, dict) for item in data):
        raise ValueError("JSON must have only dictionaries")
    
    # Get column names from first dictionary
    fieldnames = list(data[0].keys())
    
    # Create output directory
    csv_file.parent.mkdir(parents=True, exist_ok=True)
    
    # Write CSV
    with open(csv_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)