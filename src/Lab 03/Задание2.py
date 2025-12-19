import sys
import os


def normalize(text):
    text = text.lower()
    text = text.replace("ё", "е").replace("Ё", "е")
    return text


def tokenize(text):
    import re

    pattern = r"[а-яёa-z]+"
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
        with open(input_file, "r", encoding="utf-8") as f:
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
