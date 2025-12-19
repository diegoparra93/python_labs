import sys
from pathlib import Path


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    file_path = Path(path)
    return file_path.read_text(encoding=encoding)


def write_csv(rows, path: str | Path, header=None) -> None:
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
    text = text.replace("ё", "е").replace("Ё", "е")
    text = text.replace("\t", " ").replace("\r", " ").replace("\n", " ")
    text = " ".join(text.split())
    return text


def tokenize(text: str):
    import re

    pattern = r"[а-яёa-z]+"
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
