import random
from dataclasses import dataclass
from pathlib import Path
from typing import List, Tuple, Union

from attribute import Blood, BloodEnum, Sign, SignEnum, Zodiac, ZodiacEnum


@dataclass
class Unsei:
    sign: Sign
    blood: Blood
    zodiac: Zodiac
    _random_numbers: Tuple[int, int, int] = None
    _rank: int = None
    _rucky_item: str = None

    def __post_init__(self):
        # ソートの対象となる乱数を生成(重複がありうるので3重タプルにする)
        self._random_numbers = (
            random.randint(1, 10000),
            random.randint(1, 10000),
            random.randint(1, 10000),
        )

    @property
    def random_numbers(self):
        return self._random_numbers

    @property
    def rank(self):
        return self._rank

    @rank.setter
    def rank(self, rank):
        self._rank = rank

    @property
    def rucky_item(self):
        return self._rucky_item

    @rucky_item.setter
    def rucky_item(self, item):
        self._rucky_item = item

    def __repr__(self):
        return f"{self._rank}位\t{self.sign.get_name()}座 x {self.zodiac.get_name()}年 x {self.blood.get_name()}型\t{self.rucky_item}\n"


def _read_txt(input_txt_path: Path) -> List[str]:
    assert input_txt_path.exists(), f"{input_txt_path} does not exists !"
    res = []
    with open(input_txt_path, "r") as f:
        for word in f.readlines():
            res.append(word.replace("\n", ""))
    return res


def _write_txt(output_txt_path: Path, rows: List[List[Union[int, str]]]) -> None:
    with open(output_txt_path, "w") as f:
        for row in rows:
            f.write(row)


if __name__ == "__main__":

    # 名詞, 形容詞の読み込み
    nouns_path = Path("./data/noun.txt")
    adjectives_path = Path("./data/adjective.txt")
    nouns: List[str] = _read_txt(nouns_path)
    adjectives: List[str] = _read_txt(adjectives_path)

    # 運勢一覧を初期化
    unseis = []
    for sign_enum in SignEnum:
        for blood_enum in BloodEnum:
            for zodiac_enum in ZodiacEnum:
                sign = Sign(sign_enum)
                blood = Blood(blood_enum)
                zodiac = Zodiac(zodiac_enum)
                unsei = Unsei(sign, blood, zodiac)
                unseis.append(unsei)

    # 運勢一覧をソートしてランク付け
    unseis.sort(key=lambda u: u.random_numbers)
    for i, unsei in enumerate(unseis):
        unsei.rank = i + 1

    # ラッキーアイテムを付与
    for i, unsei in enumerate(unseis):
        index_noun = random.randint(0, len(nouns)-1)
        index_adjective = random.randint(0, len(adjectives)-1)
        unsei.rucky_item = f"{adjectives[index_adjective]}{nouns[index_noun]}"

    # 出力
    output_txt = Path("output.txt")
    rows = [repr(unsei) for unsei in unseis]
    _write_txt(output_txt, rows)
