import os
import copy
import csv
import random
from pathlib import Path
from typing import Any, TypeVar, Iterator
import datetime

T = TypeVar("T")


def chcek_path_exists(func):
    def check(*args):
        for arg in args:
            if os.path.splitext(arg)[-1] in [".txt", ".tsv"]:
                if not Path(arg).exists():
                    print("-" * 30)
                    print(f"{arg} does not exists!")
                    print("-" * 30)
        return func(*args)

    return check


@chcek_path_exists
def read_txt(txt_path: Path) -> list[str]:
    # assert txt_path.exists(), f"{txt_path} does not exists !"
    with open(txt_path, "r") as f:
        return [line.replace("\n", "") for line in f.readlines()]


def write_txt(txt_path: Path, rows: list[str]) -> None:
    with open(txt_path, "w") as f:
        for row in rows:
            f.write(row)


@chcek_path_exists
def read_tsv(tsv_path: Path) -> Iterator[list[str]]:
    with open(tsv_path, "r") as f:
        for row in csv.reader(f, delimiter="\t"):
            yield row


def write_tsv(tsv_path: Path, rows: list[list[str]]) -> None:
    # assert
    with open(tsv_path, "w") as f:
        writer = csv.writer(f, lineterminator="\n", delimiter="\t")
        for row in rows:
            writer.writerow(row)


def csv_to_dict(csv_path: Path) -> dict[str, Any]:
    assert csv_path.exists(), f"{csv_path} does not exists !"
    with open(csv_path, "r") as f:
        return {row[0]: row[1] for row in csv.reader(f)}


def get_shuffled_list(input_list: list[T]) -> list[T]:
    """random.shuffle has side effects, so deepcopy the original list and shuffle the copied list back."""
    copied_list: list[T] = copy.deepcopy(input_list)
    random.shuffle(copied_list)
    return copied_list


nouns_path: Path = Path("./data/noun.txt")
adjectives_path: Path = Path("./data/adjective.txt")
nouns: list[str] = read_txt(nouns_path)
adjectives: list[str] = read_txt(adjectives_path)
japanese_d: str = datetime.datetime.now().strftime("%Y年%m月%d日")
YYYYmmdd: str = datetime.datetime.now().strftime("%Y%m%d")
