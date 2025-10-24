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
![Photo 1](https://github.com/diegoparra93/python_labs/blob/main/images/lab02/lab02/01%20.png)

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
![Photo 2](https://github.com/diegoparra93/python_labs/blob/main/images/lab02/lab02/02.png)



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
![Photo3](https://github.com/diegoparra93/python_labs/blob/main/images/lab02/lab02/03.png)


##Лабораторная работа 3

### Задание 1

'''
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

'''
    




