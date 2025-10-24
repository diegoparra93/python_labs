import re

def normalize(text):
    text = text.casefold()
    text = text.replace('ё', 'е').replace('Ё', 'Е')
    text = re.sub(r'[\t\r\n]+', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def tokenize(text):
    return re.findall(r'\w+(?:-\w+)*', text)

def count_freq(tokens):
    freq = {}
    for t in tokens:
        freq[t] = freq.get(t, 0) + 1
    return freq

def top_n(freq, n=5):
    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    return sorted_items[:n]

if __name__ == "__main__":
    # Probando normalize
    print("=== normalize ===")
    tests = [
        "ПрИвЕт\nМИр\t",
        "ёжик, Ёлка",
        "  много   пробелов  "
    ]
    for test in tests:
        print(f"'{test}' -> '{normalize(test)}'")
    
    # Probando tokenize
    print("\n=== tokenize ===")
    texts = [
        "привет, мир!",
        "по-настоящему круто",
        "2025 год"
    ]
    for text in texts:
        print(f"'{text}' -> {tokenize(text)}")
    
    # Probando count_freq y top_n
    print("\n=== count_freq + top_n ===")
    words = ["a", "b", "a", "c", "b", "a"]
    freq = count_freq(words)
    top = top_n(freq, 2)
    print(f"Palabras: {words}")
    print(f"Frecuencias: {freq}")
    print(f"Top 2: {top}")
    
    # Texto en ruso completo
    print("\n=== texto ruso ===")
    texto = "Привет мир! Привет всем."
    norm = normalize(texto)
    toks = tokenize(norm)
    frec = count_freq(toks)
    top5 = top_n(frec)
    print(f"Original: {texto}")
    print(f"Tokens: {toks}")
    print(f"Top 5: {top5}")