## Python Labs
[Python Lab01](/README_files/lab01_readme.md)

## Python Labs 2
[Python Lab02](/README_files/lab01_readme.md)

### Задание 1
```
def min_max(nums):
    if not nums:
        return ValueError
    
    max_val = nums[0]
    min_val = nums[0]
    
    for num in nums:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num
    
    return (min_val, max_val)


def unique_sorted(nums):
    return sorted(set(nums))


def flatten(mat):
    if not mat:
        return []
    
    result = []
    
    for item in mat:
        if not isinstance(item, (list, tuple)):
            return TypeError
        result.extend(item)
    
    return result
```
![Photo 1](https://github.com/diegoparra93/python_labs/blob/main/images/lab02/01%20.png)

### Задание 2
```
def transpose(mat):
    # If esta vacio, uso esta formula. 
    if mat == []:
        return []
    
    # Check el tamano del primer row
    size = len(mat[0])
    
    # проверьте, имеют ли все строки одинаковый размер - verificar si todas las rows tienen el mismo tamano
    for row in mat:
        if len(row) != size:
            raise ValueError("not rectangular")
    
    new_matrix = []
    
    # Para cada columna - для каждого столбца
    for j in range(len(mat[0])):
        new_row = []
        # For each row  
        for i in range(len(mat)):
            new_row.append(mat[i][j])
        new_matrix.append(new_row)
    
    return new_matrix

def row_sums(mat):
    if mat == []:
        return []
    
    # Check if rectangular - проверьте, является ли он прямоугольным
    first_size = len(mat[0])
    for row in mat:
        if len(row) != first_size:
            raise ValueError("different rows")
    
    results = []
    for row in mat:
        # Sum the row
        total = 0
        for number in row:
            total += number
        results.append(total)
    
    return results

def col_sums(mat):
    if not mat:
        return []
    
    # Check if all rows same size
    size = len(mat[0])
    for row in mat:
        if len(row) != size:
            raise ValueError("weird matrix")
    
    sums = []
    # For each column
    for col in range(len(mat[0])):
        s = 0
        # Sum that column in all rows
        for row in range(len(mat)):
            s = s + mat[row][col]
        sums.append(s)
    
    return sums
```
![Photo 2](https://github.com/diegoparra93/python_labs/blob/main/images/lab02/02.png)



### Задание 3

```
def format_record(rec: tuple[str, str, float]) -> str:
    
    if not isinstance(rec, tuple):
        raise TypeError("Input must be a tuple")
    
    if len(rec) != 3:
        raise ValueError("Tuple must have exactly 3 elements")
    
    name, group, grade = rec
    
    if not isinstance(name, str):
        raise TypeError("Name must be a string")
    
    if not isinstance(group, str):
        raise TypeError("Group must be a string")
    
    if not isinstance(grade, (int, float)):
        raise TypeError("GPA must be a number")
    
    if not name.strip():
        raise ValueError("Name cannot be empty")
    
    if not group.strip():
        raise ValueError("Group cannot be empty")
    
    if grade < 0:
        raise ValueError("GPA cannot be negative")
    
    name = name.strip()
    while "  " in name:
        name = name.replace("  ", " ")

    name = name.title()

    parts = name.split()
    last_name = parts[0]
 
    initials = ""
    if len(parts) > 1:
        initials = parts[1][0] + "."
    if len(parts) > 2:
     initials = initials + parts[2][0] + "."
    gpa_str = f"{grade:.2f}"

    result = last_name + " " + initials + ", gr. " + group + ", GPA " + gpa_str
    
    return result
```
![Photo3](https://github.com/diegoparra93/python_labs/blob/main/images/lab02/03.png)


## Лабораторная работа 3

### Задание 1

```

def normalize(text):
    text = text.lower()
    replacements = {
        'ё': 'е',
        'Ё': 'е'
    }
    
    for old, new in replacements.items():
        text = text.replace(old, new)
    
    return text

def tokenize(text):
    import re
    pattern = r'[а-яёa-z]+'
    tokens = re.findall(pattern, text, re.IGNORECASE)
    return tokens

def count_freq(tokens):
    freq = {}
    for token in tokens:
        token = token.lower()
        freq[token] = freq.get(token, 0) + 1
    return freq

def top_n(freq_dict, n):
    sorted_items = sorted(freq_dict.items(), key=lambda x: (-x[1], x[0]))
    return sorted_items[:n]

print("\n--- normalize() ---")
test_cases = [
    "ПрИвЕт\nМИр\t",
    "ёжик, Ёлка", 
    "Hello\r\nWorld",
    "  двойные   пробелы  ",
    "Привет! Как дела?"
]

for i, test in enumerate(test_cases, 1):
    result = normalize(test)
    print(f"Test {i}: '{test}' → '{result}'")

print("\n--- tokenize() ---")
token_tests = [
    "привет мир",
    "hello,world!!!",
    "по-настоящему круто",
    "2025 год",
    "emoji 😀 не слово",
    "цена 100-200 рублей"
]

for i, test in enumerate(token_tests, 1):
    result = tokenize(test)
    print(f"Test {i}: '{test}' → {result}")

print("\n--- count_freq() + top_n() ---")

tokens1 = ["a", "b", "a", "c", "b", "a"]
freq1 = count_freq(tokens1)
top1 = top_n(freq1, 2)
print(f"Tokens: {tokens1}")
print(f"Frecuencias: {freq1}")
print(f"Top 2: {top1}")

tokens2 = ["bb", "aa", "bb", "aa", "cc"]
freq2 = count_freq(tokens2)
top2 = top_n(freq2, 3)
print(f"\nTokens: {tokens2}")
print(f"Frecuencias: {freq2}")
print(f"Top 3: {top2}")

print("\n--- Texto real ruso ---")
texto_ruso = "привет мир привет всем мир привет"
tokens_ruso = tokenize(texto_ruso)
freq_ruso = count_freq(tokens_ruso)
top_ruso = top_n(freq_ruso, 5)

print(f"Texto: '{texto_ruso}'")
print(f"Tokens: {tokens_ruso}")
print(f"Frecuencias: {freq_ruso}")
print(f"Top 5: {top_ruso}")

if __name__ == "__main__":
    pass

```
![photo 1](https://github.com/diegoparra93/python_labs/blob/main/images/Lab03/Lab3_1.1.png)

### Задание 2

```
import sys
import os

def normalize(text):
    text = text.lower()
    text = text.replace('ё', 'е').replace('Ё', 'е')
    return text

def tokenize(text):
    import re
    pattern = r'[а-яёa-z]+'
    tokens = re.findall(pattern, text, re.IGNORECASE)
    return tokens

def count_freq(tokens):
    freq = {}
    for token in tokens:
        token = token.lower()
        freq[token] = freq.get(token, 0) + 1
    return freq

def top_n(freq_dict, n):
    sorted_items = sorted(freq_dict.items(), key=lambda x: (-x[1], x[0]))
    return sorted_items[:n]

def main():
    # Obtener la ruta base del proyecto
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    input_file = os.path.join(base_dir, "data", "lab04", "input.txt")
    
    # Verificar si hay entrada por stdin, sino usar el archivo
    if not sys.stdin.isatty():
        text = sys.stdin.read()
    else:
        # Leer del archivo por defecto
        with open(input_file, 'r', encoding='utf-8') as f:
            text = f.read()
    
    if not text.strip():
        print("No input provided")
        return
    
    norm_text = normalize(text)
    tokens = tokenize(norm_text)
    freq = count_freq(tokens)
    top = top_n(freq, 5)

    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freq)}")
    print("Топ-5:")
    for word, count in top:
        print(f"{word}:{count}")

if __name__ == "__main__":
    main()
```

![Photo 2](https://github.com/diegoparra93/python_labs/blob/main/images/Lab03/Lab3_2task.png)


## Лабораторная работа 4

### Задание 1

```
import csv
from pathlib import Path
from typing import Iterable, Sequence, Union


def read_text(path: Union[str, Path], encoding: str = "utf-8") -> str:
    p = Path(path)
    return p.read_text(encoding=encoding)


def write_csv(rows: Iterable[Sequence], path: Union[str, Path],
              header: tuple[str, ...] | None = None) -> None:
    p = Path(path)
    rows_list = list(rows)
    
    if rows_list:
        first_len = len(rows_list[0])
        for i, row in enumerate(rows_list):
            if len(row) != first_len:
                raise ValueError(f"Row {i} has different length")
    
    ensure_parent_dir(p)
    
    with p.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if header is not None:
            writer.writerow(header)
        writer.writerows(rows_list)


def ensure_parent_dir(path: Union[str, Path]) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)


if __name__ == "__main__":
    print("=== Testing io_txt_csv ===")
    
    txt = read_text("data/lab04/input.txt")
    print("Read text:")
    print(repr(txt))
    print(f"Text length: {len(txt)} characters")
    
    write_csv([("word", "count"), ("test", 3)], "data/lab04/check.csv")
    print("CSV created: data/lab04/check.csv")
    
    with open("data/lab04/check.csv", "r", encoding="utf-8") as f:
        print("CSV content:")
        print(f.read())
```
![photo 1](https://github.com/diegoparra93/python_labs/blob/main/images/Lab04/Lab4_1task.png)

### Задание 1

```
import sys
from pathlib import Path

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    file_path = Path(path)
    return file_path.read_text(encoding=encoding)

def write_csv(rows, path: str | Path, header = None) -> None:
    import csv
    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    
    with file_path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        if header is not None:
            writer.writerow(header)
        writer.writerows(rows)

def normalize(text: str) -> str:
    text = text.lower()
    text = text.replace('ё', 'е').replace('Ё', 'е')
    text = text.replace('\t', ' ').replace('\r', ' ').replace('\n', ' ')
    text = ' '.join(text.split())
    return text

def tokenize(text: str):
    import re
    pattern = r'[а-яёa-z]+'
    tokens = re.findall(pattern, text, re.IGNORECASE)
    return tokens

def count_freq(tokens):
    frequency = {}
    for token in tokens:
        token = token.lower()
        frequency[token] = frequency.get(token, 0) + 1
    return frequency

def top_n(freq_dict, n: int):
    sorted_items = sorted(freq_dict.items(), key=lambda x: (-x[1], x[0]))
    return sorted_items[:n]

def process_single_file(input_file: str, output_file: str) -> None:
    try:
        text_content = read_text(input_file)
        print(f"✓ Read File : {input_file}")

        clean_text = normalize(text_content)
        words = tokenize(clean_text)
        frequencies = count_freq(words)
        top_words = top_n(frequencies, 5)

        total_words = len(words)
        unique_words = len(frequencies)

        print(f"Всего слов: {total_words}")
        print(f"Уникальных слов: {unique_words}")
        print("Топ-5:")
        for word, count in top_words:
            print(f"{word}:{count}")

        # Preparar datos para CSV
        all_word_counts = []
        for word, count in frequencies.items():
            all_word_counts.append((word, count))
        
        # Ordenar por frecuencia
        all_word_counts.sort(key=lambda x: (-x[1], x[0]))
        
        # Escribir CSV
        write_csv(all_word_counts, output_file, header=("word", "count"))
        
        
    except FileNotFoundError:
        print(f"❌ Error: No se encontró el archivo {input_file}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

def main():
    input_file = "data/lab04/input.txt"
    output_file = "data/lab04/report.csv"
    
    print("=== Генератор отчетов текстовой статистики ===")
    print(f"Входной файл: {input_file}")
    print(f"Выходной файл: {output_file}")
    print("-" * 50)
    
    process_single_file(input_file, output_file)
    
    print("-" * 50)
    print("✅ Готово! Отчет создан успешно.")

if __name__ == "__main__":
    main()
```
![Photo 2](https://github.com/diegoparra93/python_labs/blob/main/images/Lab04/Lab4_2task.png)

## Лабораторная работа 5

### Задание 1
```
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

```
![Photo1](https://github.com/diegoparra93/python_labs/blob/main/images/Lab05/Screenshot%202025-11-21%20at%2011.10.35.png)
### Задание 2
```
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
```
![Photo 2](https://github.com/diegoparra93/python_labs/blob/main/images/Lab05/Screenshot%202025-11-21%20at%2011.12.30.png)
![photo 3](https://github.com/diegoparra93/python_labs/blob/main/images/Lab05/Screenshot%202025-11-21%20at%2011.12.47.png)
![photo 4](https://github.com/diegoparra93/python_labs/blob/main/images/Lab05/Screenshot%202025-11-21%20at%2011.13.07.png)
![photo 5](https://github.com/diegoparra93/python_labs/blob/main/images/Lab05/Screenshot%202025-11-21%20at%2011.29.14.png)


## Лабораторная работа 7


### Задание A

```
# src/lib/text.py
# Simple text utilities used in labs


def normalize(text: str) -> str:
    """
    Normalize text: convert to lower case, replace CR/LF/TAB with spaces,
    collapse multiple whitespace into a single space, strip edges.
    """
    s = text.replace("\r", " ").replace("\n", " ").replace("\t", " ")
    s = s.lower()

    # REQUIRED: replace Cyrillic ё with е
    s = s.replace("ё", "е")

    parts = s.split()  # splits on any whitespace and collapses
    return " ".join(parts)


def tokenize(text: str) -> list[str]:
    """
    Naive tokenization: normalize, split on whitespace, strip punctuation on edges.
    Returns list of tokens (strings).
    """
    import string

    norm = normalize(text)
    tokens: list[str] = []
    for tok in norm.split():
        tok = tok.strip(string.punctuation + "«»“”—…")
        if tok:
            tokens.append(tok)
    return tokens


def count_freq(tokens: list[str]) -> dict[str, int]:
    """
    Count frequency of tokens. Returns dict token -> count.
    """
    freq: dict[str, int] = {}
    for t in tokens:
        freq[t] = freq.get(t, 0) + 1
    return freq


def top_n(freq: dict[str, int], n: int) -> list[tuple[str, int]]:
    """
    Return top n items sorted by frequency descending.
    For ties (same frequency) sorts words alphabetically ascending.
    Returns list of (word, count).
    """
    items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    return items[:n]
```
### Задание B - Тесты для src/lab05/json_csv.py

```
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
```
![Photo A](https://github.com/diegoparra93/python_labs/blob/main/images/lab07/A.png)
![Photo B](https://github.com/diegoparra93/python_labs/blob/main/images/lab07/B.png)
![Photo C](https://github.com/diegoparra93/python_labs/blob/main/images/lab07/C.png)
![Photo D]()https://github.com/diegoparra93/python_labs/blob/main/images/lab07/D.png


