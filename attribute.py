from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import NamedTuple

ZODIACS = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]
BLOODS = ["A", "B", "O", "AB"]
SIGNS = [
    "おひつじ",
    "おうし",
    "ふたご",
    "かに",
    "しし",
    "おとめ",
    "てんびん",
    "さそり",
    "いて",
    "やぎ",
    "みずがめ",
    "うお",
]
IMG_ROOT = Path("imgs")


class ZodiacEnum(Enum):
    # ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]
    NE = 0
    USHI = 1
    TORA = 2
    U = 3
    TATSU = 4
    MI = 5
    UMA = 6
    HITSUJI = 7
    SARU = 8
    TORI = 9
    INU = 10
    I = 11


class BloodEnum(Enum):
    A = 0
    B = 1
    O = 2
    AB = 3


class SignEnum(Enum):
    OHITSUJI = 0
    OUSHI = 1
    HUTAGO = 2
    KANI = 3
    SHISHI = 4
    OTOME = 5
    TENBIN = 6
    SASORI = 7
    ITE = 8
    YAGI = 9
    MIZUGAME = 10
    UO = 11


@dataclass
class Zodiac:
    no: ZodiacEnum
    path: Path = None
    path_gh: str = None

    def __post_init__(self):
        self.path = next(
            (IMG_ROOT / "eto").glob(f"eto_mark{self.no.value + 1 :02}_*png")
        )
        self.path_gh = "<img src='" + '/'.join(str(self.path).split('/')[:2]) + '/small/' + '/'.join(str(self.path).split('/')[2:]) + "'>"

    def get_name(self):
        return ZODIACS[self.no.value]


    @classmethod
    def get_zodiac_by_string(cls, s: str):
        zodiac_enum = ZodiacEnum(ZODIACS.index(s))
        return Zodiac(zodiac_enum)


@dataclass
class Blood:
    no: BloodEnum
    path: Path = None
    path_gh: str = None

    def __post_init__(self):
        self.path = IMG_ROOT / f"blood/ketsuekigata_{(self.no.name).lower()}.png"
        self.path_gh = "<img src='" + '/'.join(str(self.path).split('/')[:2]) + '/small/' + '/'.join(str(self.path).split('/')[2:]) + "'>"

    def get_name(self):
        return BLOODS[self.no.value]

    @classmethod
    def get_blood_by_string(cls, s: str):
        blood_enum = BloodEnum(BLOODS.index(s))
        return Blood(blood_enum)


@dataclass
class Sign:
    no: SignEnum
    path: Path = None
    path_gh: str = None

    def __post_init__(self):
        self.path = next(
            (IMG_ROOT / "sign").glob(f"seiza_mark{self.no.value + 1 :02}_*.png")
        )
        self.path_gh = "<img src='" + '/'.join(str(self.path).split('/')[:2]) + '/small/' + '/'.join(str(self.path).split('/')[2:]) + "'>"

    def get_name(self):
        return SIGNS[self.no.value]

    @classmethod
    def get_sign_by_string(cls, s: str):
        sign_enum = SignEnum(SIGNS.index(s))
        return Sign(sign_enum)
