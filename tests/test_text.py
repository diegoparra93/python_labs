import pytest
from src.lib.text import normalize, tokenize, count_freq, top_n


# ---------- TESTS FOR normalize ----------
@pytest.mark.parametrize(
    "source, expected",
    [
        ("ПрИвЕт\nМИр\t", "привет мир"),
        ("ёжик, Ёлка", "ежик, елка"),
        ("Hello\r\nWorld", "hello world"),
        ("  двойные   пробелы  ", "двойные пробелы"),
        ("", ""),  # empty input
    ],
)
def test_normalize(source, expected):
    assert normalize(source) == expected


# ---------- TESTS FOR tokenize ----------
@pytest.mark.parametrize(
    "source, expected_tokens",
    [
        ("hello world", ["hello", "world"]),
        ("  spaces  and, commas! ", ["spaces", "and", "commas"]),
        ("punctuation: end.", ["punctuation", "end"]),
        ("mixed CASE", ["mixed", "case"]),
        ("", []),  # empty
    ]
)
def test_tokenize(source, expected_tokens):
    assert tokenize(source) == expected_tokens


# ---------- TESTS FOR count_freq + top_n ----------
def test_count_freq_and_top_n():
    tokens = ["a", "b", "a", "c", "b", "a"]
    freq = count_freq(tokens)

    assert freq == {"a": 3, "b": 2, "c": 1}

    top2 = top_n(freq, 2)
    assert top2 == [("a", 3), ("b", 2)]


# ---------- TESTS FOR top_n tie sorting ----------
def test_top_n_tie_breaker():
    tokens = ["a", "b", "b", "a", "c"]

    freq = count_freq(tokens)  # a:2, b:2, c:1
    top2 = top_n(freq, 2)

    # a and b both have freq=2 → alphabetical order → a before b
    assert top2 == [("a", 2), ("b", 2)]
