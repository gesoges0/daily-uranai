import random
from collections import deque
from dataclasses import dataclass
from itertools import product
from pathlib import Path
from typing import List, NamedTuple, Tuple, Union

from attribute import Eto, EtoEnum, Ketsuekigata, KetsuekigataEnum, Seiza, SeizaEnum
from utils import adjectives, get_shuffled_list, nouns, write_tsv, YYYYmmdd


@dataclass(frozen=True)
class LuckyItem:
    """
    (noun, adjective) word
    """

    noun: str
    adjective: str

    @classmethod
    def generate(cls):
        noun: str = nouns[random.randint(0, len(nouns) - 1)]
        adjective: str = adjectives[random.randint(0, len(adjectives) - 1)]
        return LuckyItem(noun, adjective)

    @property
    def name(self) -> str:
        return f"{self.adjective}{self.noun}"


class Attribute(NamedTuple):
    eto: Eto
    ketsuekigata: Ketsuekigata
    seiza: Seiza


@dataclass(frozen=True)
class Unsei:
    """
    (eto, ketusekigata, seiza)
    """

    attribute: Attribute
    lucky_item: LuckyItem
    rank: int

    @property
    def info(self) -> list[str]:
        # return f"{self.rank}位\t{self.attribute.ketsuekigata.name}型 x {self.attribute.seiza.name}座 x {self.attribute.eto.name}年\t{self.lucky_item.name}\n"
        return [
            f"{self.rank}位",  # 0
            f"{self.attribute.ketsuekigata.name}型",
            f"{self.attribute.seiza.name}座",
            f"{self.attribute.eto.name}年",
            f"{self.lucky_item.name}",  # 4
            f"{self.attribute.ketsuekigata.github_path}",
            f"{self.attribute.seiza.github_path}",
            f"{self.attribute.eto.github_path}",
        ]


if __name__ == "__main__":

    # initialize unseis
    attributes: list[Unsei] = [
        Attribute(
            eto=Eto.from_enum(ee),
            ketsuekigata=Ketsuekigata.from_enum(ke),
            seiza=Seiza.from_enum(se),
        )
        for ee, ke, se in product(EtoEnum, KetsuekigataEnum, SeizaEnum)
    ]

    # make ranking
    unseis: list[Unsei] = [
        Unsei(attribute=attribute, lucky_item=LuckyItem.generate(), rank=no + 1)
        for no, attribute in enumerate(get_shuffled_list(attributes))
    ]

    # output
    output_tsv: Path = Path(f"./output/ranking_{YYYYmmdd}.tsv")
    write_tsv(output_tsv, [unsei.info for unsei in unseis])
