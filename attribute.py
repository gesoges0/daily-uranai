from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import NamedTuple

from utils import csv_to_dict

IMG_ROOT = Path("imgs")

eto_name_by_eto_enum: dict = csv_to_dict(Path("attribute/eto.csv"))
ketsuekigata_name_by_ketsuekigata_enum: dict = csv_to_dict(
    Path("attribute/ketsuekigata.csv")
)
seiza_name_by_seiza_enum: dict = csv_to_dict(Path("attribute/seiza.csv"))


class EtoEnum(Enum):
    ne = 0
    ushi = 1
    tora = 2
    u = 3
    tatsu = 4
    mi = 5
    uma = 6
    hitsuji = 7
    saru = 8
    tori = 9
    inu = 10
    i = 11


class KetsuekigataEnum(Enum):
    a = 0
    b = 1
    o = 2
    ab = 3


class SeizaEnum(Enum):
    ohitsuji = 0
    oushi = 1
    futago = 2
    kani = 3
    shishi = 4
    otome = 5
    tenbin = 6
    sasori = 7
    ite = 8
    yagi = 9
    mizugame = 10
    uo = 11


@dataclass(frozen=True)
class Base(ABC):
    path: Path
    # path_for_github: str

    @classmethod
    @abstractmethod
    def from_enum(self, e: Enum):
        raise NotImplementedError()

    @property
    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError()

    @property
    def github_path(self) -> str:
        # for github readme markdown path
        return f"<img src='{str(self.path)}'>"


@dataclass(frozen=True)
class Eto(Base):
    e: EtoEnum

    @classmethod
    def from_enum(self, e: EtoEnum):
        path: Path = IMG_ROOT / "eto" / "small" / f"{e.name}.png"
        return Eto(e=e, path=path)

    @property
    def name(self) -> str:
        return eto_name_by_eto_enum[self.e.name]


@dataclass(frozen=True)
class Ketsuekigata(Base):
    e: KetsuekigataEnum

    @classmethod
    def from_enum(self, e: KetsuekigataEnum):
        path: Path = IMG_ROOT / "ketsuekigata" / "small" / f"{e.name}.png"
        return Ketsuekigata(e=e, path=path)

    @property
    def name(self) -> str:
        return ketsuekigata_name_by_ketsuekigata_enum[self.e.name]


@dataclass(frozen=True)
class Seiza(Base):
    e: SeizaEnum

    @classmethod
    def from_enum(self, e: SeizaEnum):
        path: Path = IMG_ROOT / "seiza" / "small" / f"{e.name}.png"
        return Seiza(e=e, path=path)

    @property
    def name(self) -> str:
        return seiza_name_by_seiza_enum[self.e.name]
