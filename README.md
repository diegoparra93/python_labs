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
![Photo D](https://github.com/diegoparra93/python_labs/blob/main/images/lab07/D.png)


## Лабораторная работа 8

### A. Student (models.py)
```
from dataclasses import dataclass
from datetime import datetime, date

@dataclass
class Student:
    """
    Student class with COMPLETE VALIDATION (like your friend's)
    """
    full_name: str          # Student's full name
    birthdate: str          # Birth date in YYYY-MM-DD format
    group: str              # Study group
    gpa: float             # Grade point average (0-5)

    def __post_init__(self):
        """
        Validate ALL fields after object creation
        """
        self._validate_full_name()
        self._validate_birthdate()
        self._validate_group()
        self._validate_gpa()
        print(f"✅ Student {self.full_name} created successfully!")

    # ========== VALIDATION METHODS ==========

    def _validate_full_name(self):
        """Validate full name (like your friend's version)"""
        # 1. Check type
        if not isinstance(self.full_name, str):
            raise TypeError("Full name must be a string")
        
        # 2. Check not empty
        if len(self.full_name.strip()) == 0:
            raise TypeError("Full name cannot be empty")
        
        # 3. Check characters (only letters, spaces, hyphen)
        for char in self.full_name:
            if not (char.isalpha() or char.isspace() or char == "-"):
                raise TypeError("Full name can only contain letters, spaces, and hyphen")
        
        # 4. Minimum 2 words (name and surname)
        name_parts = self.full_name.split()
        if len(name_parts) < 2:
            raise TypeError("Full name must contain at least 2 words (name and surname)")
        
        # 5. Each word starts with capital letter
        for name_part in name_parts:
            if not name_part[0].isupper():
                raise TypeError("Each word in full name must start with a capital letter")

    def _validate_birthdate(self):
        """Validate birth date (improved version)"""
        # 1. Check type
        if not isinstance(self.birthdate, str):
            raise ValueError("Birthdate must be a string")
        
        # 2. Check length (YYYY-MM-DD = 10 characters)
        if len(self.birthdate) != 10:
            raise ValueError("Birthdate must be in YYYY-MM-DD format (10 characters)")
        
        # 3. Check separators
        if self.birthdate[4] != "-" or self.birthdate[7] != "-":
            raise ValueError("Birthdate must be in YYYY-MM-DD format")
        
        # 4. Check all parts are digits
        year_part = self.birthdate[0:4]
        month_part = self.birthdate[5:7]
        day_part = self.birthdate[8:10]
        
        if not (year_part.isdigit() and month_part.isdigit() and day_part.isdigit()):
            raise TypeError("Birthdate can only contain digits")
        
        # 5. Check if date is valid
        try:
            birth_date = datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Invalid birthdate (e.g., 2025-13-45)")
        
        # 6. Check date is not in the future
        today = date.today()
        if birth_date > today:
            raise ValueError("Birthdate cannot be in the future")

    def _validate_gpa(self):
        """Validate grade point average"""
        # 1. Check type (must be float or int)
        if not isinstance(self.gpa, (int, float)):
            raise TypeError("GPA must be a number (float or int)")
        
        # 2. Convert int to float if needed
        if isinstance(self.gpa, int):
            self.gpa = float(self.gpa)
        
        # 3. Check range 0-5
        if not (0 <= self.gpa <= 5):
            raise ValueError(f"GPA must be between 0 and 5. Yours: {self.gpa}")

    def _validate_group(self):
        """Validate group number"""
        # 1. Check type
        if not isinstance(self.group, str):
            raise TypeError("Group must be a string")
        
        # 2. Check not empty
        if not self.group.strip():
            raise ValueError("Group cannot be empty")
        
        # 3. Check minimum length (at least 5 characters)
        if len(self.group) < 5:
            raise ValueError("Group is too short (minimum 5 characters)")

    # ========== MAIN METHODS ==========

    def age(self) -> int:
        """Calculate student's age in full years"""
        birth_date = datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        today = date.today()
        
        age = today.year - birth_date.year
        
        # If birthday hasn't occurred yet this year
        if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
            age -= 1
        
        return age

    def to_dict(self) -> dict:
        """Convert object to dictionary for JSON"""
        # Check all fields are filled
        if not self.full_name or not self.full_name.strip():
            raise ValueError("Field 'full_name' cannot be empty")
        
        if not self.birthdate or not self.birthdate.strip():
            raise ValueError("Field 'birthdate' cannot be empty")
        
        if not self.group or not self.group.strip():
            raise ValueError("Field 'group' cannot be empty")
        
        if self.gpa is None:
            raise ValueError("Field 'gpa' cannot be None")
        
        # Return dictionary
        return {
            "full_name": self.full_name,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa
        }

    @classmethod
    def from_dict(cls, data: dict):
        """Create Student object from dictionary"""
        return cls(
            full_name=data['full_name'],
            birthdate=data['birthdate'],
            group=data['group'],
            gpa=data['gpa']
        )

    def __str__(self) -> str:
        """Pretty string representation"""
        return f"👨‍🎓 {self.full_name} | Group: {self.group} | GPA: {self.gpa} | Age: {self.age()} years"
```
### B. Serialize.py

```
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
```
![Photo A](https://github.com/diegoparra93/python_labs/blob/main/images/Lab08/a.png)
![Photo A](https://github.com/diegoparra93/python_labs/blob/main/images/Lab08/b.png)
![Photo A](https://github.com/diegoparra93/python_labs/blob/main/images/Lab08/c.png)


## Лабораторная работа 9

### Задание А-B

```
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

```

![Photo A](https://github.com/diegoparra93/python_labs/blob/main/images/Lab09/Lab9A.png)
![Photo B](https://github.com/diegoparra93/python_labs/blob/main/images/Lab09/Lab9B.png)


## Лабораторная работа 10

### A. sctrucutre.py
```
from collections import deque

class Stack:
    def __init__(self):
        self._data = []
    
    def push(self, item):
        self._data.append(item)
    
    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self._data.pop()
    
    def peek(self):
        if self.is_empty():
            return None
        return self._data[-1]
    
    def is_empty(self):
        return len(self._data) == 0
    
    def __len__(self):
        return len(self._data)
    
    def __repr__(self):
        return f"Stack({self._data})"

class Queue:
    def __init__(self):
        self._data = deque()
    
    def enqueue(self, item):
        self._data.append(item)
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self._data.popleft()
    
    def peek(self):
        if self.is_empty():
            return None
        return self._data[0]
    
    def is_empty(self):
        return len(self._data) == 0
    
    def __len__(self):
        return len(self._data)
    
    def __repr__(self):
        return f"Queue({list(self._data)})"
        ```

### B - Linked.list.py

```
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __repr__(self):
        return f"Node({self.value})"

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1
    
    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        if self.tail is None:
            self.tail = new_node
        self._size += 1
    
    def insert(self, idx, value):
        if idx < 0 or idx > self._size:
            raise IndexError(f"Index {idx} out of bounds")
        
        if idx == 0:
            self.prepend(value)
            return
        if idx == self._size:
            self.append(value)
            return
        
        new_node = Node(value)
        current = self.head
        for _ in range(idx - 1):
            current = current.next
        new_node.next = current.next
        current.next = new_node
        self._size += 1
    
    def remove(self, value):
        if self.head is None:
            return
        
        if self.head.value == value:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self._size -= 1
            return
        
        current = self.head
        while current.next and current.next.value != value:
            current = current.next
        
        if current.next:
            if current.next == self.tail:
                self.tail = current
            current.next = current.next.next
            self._size -= 1
    
    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next
    
    def __len__(self):
        return self._size
    
    def __repr__(self):
        values = list(self)
        return f"SinglyLinkedList({values})"
    
    def display(self):
        current = self.head
        result = []
        while current:
            result.append(f"[{current.value}]")
            current = current.next
        result.append("None")
        return " -> ".join(result)
        ```
### _init_,py      

```
from .structures import Stack, Queue
from .linked_list import Node, SinglyLinkedList

__all__ = ['Stack', 'Queue', 'Node', 'SinglyLinkedList']
```
