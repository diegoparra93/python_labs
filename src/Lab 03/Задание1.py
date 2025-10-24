# 3aqawwel.py

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