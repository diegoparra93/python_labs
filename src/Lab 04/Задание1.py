import csv
from pathlib import Path
from typing import Iterable, Sequence, Union


def read_text(path: Union[str, Path], encoding: str = "utf-8") -> str:
    p = Path(path)

    return p.read_text(encoding=encoding)


def write_csv(
    rows: Iterable[Sequence],
    path: Union[str, Path],
    header: tuple[str, ...] | None = None,
) -> None:
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


write_csv(["word", "word"], "./some.json")
