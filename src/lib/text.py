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
