import re


def normalize(text):
    if not isinstance(text, str):
        return ""

    text = text.lower()
    text = text.replace("ё", "е")
    text = re.sub(r"\s+", " ", text)  # Reemplaza todos los espacios múltiples
    return text.strip()


def tokenize(text):
    words = []
    current_word = ""

    for char in text:
        if char.isalpha() or char == "-":
            current_word += char
        else:
            if current_word:
                words.append(current_word)
                current_word = ""

    if current_word:
        words.append(current_word)

    return words


def count_freq(tokens):
    freq = {}
    for word in tokens:
        freq[word] = freq.get(word, 0) + 1
    return freq


def top_n(freq, n=5):
    items = list(freq.items())
    items.sort(key=lambda x: (-x[1], x[0]))
    return items[:n]


if __name__ == "__main__":
    # Pruebas
    texto = "Hello world hello friends"
    print("Texto:", texto)

    norm = normalize(texto)
    print("Normalizado:", norm)

    tokens = tokenize(norm)
    print("Tokens:", tokens)

    freq = count_freq(tokens)
    print("Frecuencias:", freq)

    top = top_n(freq, 3)
    print("Top 3:", top)
