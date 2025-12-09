import json
import csv
import pytest
from pathlib import Path
from src.lab05.json_csv import json_to_csv, csv_to_json


# ---------- JSON → CSV ----------
def test_json_to_csv_roundtrip(tmp_path: Path):
    src = tmp_path / "people.json"
    dst = tmp_path / "people.csv"

    data = [
        {"name": "Alice", "age": 22},
        {"name": "Bob", "age": 25},
    ]

    src.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    json_to_csv(str(src), str(dst))

    with dst.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    assert len(rows) == 2
    assert set(rows[0].keys()) == {"name", "age"}


# ---------- CSV → JSON ----------
def test_csv_to_json_roundtrip(tmp_path: Path):
    src = tmp_path / "people.csv"
    dst = tmp_path / "people.json"

    with src.open('w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['name', 'age'])
        writer.writeheader()
        writer.writerow({'name': 'Alice', 'age': '22'})
        writer.writerow({'name': 'Bob', 'age': '25'})

    csv_to_json(str(src), str(dst))

    data = json.loads(dst.read_text(encoding='utf-8'))
    assert len(data) == 2
    assert set(data[0].keys()) == {"name", "age"}


# ---------- NEGATIVE CASES ----------
def test_json_to_csv_empty_raises(tmp_path: Path):
    src = tmp_path / "empty.json"
    src.write_text("[]", encoding="utf-8")
    dst = tmp_path / "o.csv"

    with pytest.raises(ValueError):
        json_to_csv(str(src), str(dst))


def test_csv_to_json_empty_raises(tmp_path: Path):
    src = tmp_path / "empty.csv"
    src.write_text("", encoding="utf-8")
    dst = tmp_path / "o.json"

    with pytest.raises(ValueError):
        csv_to_json(str(src), str(dst))
