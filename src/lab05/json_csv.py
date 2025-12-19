# src/lab05/json_csv.py
import json
import csv
from typing import List, Dict


def json_to_csv(src_path: str, dst_path: str) -> None:
    """
    Read JSON file at src_path (expected: list of dicts) and write a CSV to dst_path.
    Raises ValueError for empty list or invalid JSON structure.
    """
    with open(src_path, encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, list):
        raise ValueError("JSON must contain a list of objects")

    if len(data) == 0:
        raise ValueError("JSON list is empty")

    headers = list(data[0].keys())
    with open(dst_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        for obj in data:
            writer.writerow(obj)


def csv_to_json(src_path: str, dst_path: str) -> None:
    """
    Read CSV file and dump rows as a JSON list to dst_path.
    Raises ValueError for empty CSV.
    """
    with open(src_path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    if not rows:
        raise ValueError("CSV is empty")

    with open(dst_path, "w", encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)
