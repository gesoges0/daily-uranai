from typing import List, Tuple
import csv
from pathlib import Path
from dataclasses import dataclass
import random

@dataclass
class Unsei:
    sign: str
    blood: str
    zodiac: str
    _rank: int = None
    _rucky_item: str = None

    @property
    def rank(self):
        return _rank

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
        return f'{self._rank}位\t{self.sign}x{self.zodiac}x{self.blood}型\t{self.rucky_item}\n'
    

SIGNS = ['おひつじ座', 'おうし座', 'ふたご座', 'かに座', 'しし座', 'おとめ座', 'てんびん座', 'さそり座', 'いて座', 'やぎ座', 'みずがめ座', 'うお座']
BLOODS = ['A', 'B', 'O', 'AB']
ZODIACS = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']


def _read_txt(txt_path: Path) -> List[str]:
    assert txt_path.exists(), f'{txt_path} does not exists !'
    res = []
    with open(txt_path, 'r') as f:
        for word in f.readlines():
            res.append(word.replace('\n', ''))
    return res


def _get_rucky_item_index(n: int, m: int) -> Tuple[int, int]:
    """
    return (a, b) s.t. a in [0,n), b in [0,m)
    """
    a = random.randint(0, n-1)
    b = random.randint(0, m-1)
    return (a, b)


if __name__== '__main__':
    nouns_path = Path('./data/noun.txt')
    adjectives_path = Path('./data/adjective.txt')


    # 名詞, 形容詞読み込み
    nouns: List[str] = _read_txt(nouns_path)
    adjectives: List[str] = _read_txt(adjectives_path)

    # 12 x 12 x 4 = 576個分の組合せを用意
    # (形容詞リストのインデックス, 名詞リストのインデックス) のリストを用意
    rucky_item_indices = set()
    for i in range(576):
        while True:
            rucky_item_index: Tuple[int, int] = _get_rucky_item_index(len(nouns), len(adjectives))
            if rucky_item_index not in rucky_item_indices:
                rucky_item_indices.add(rucky_item_index)
                break
    rucky_item_indices = random.sample(list(rucky_item_indices), len(rucky_item_indices))

    # 運勢一覧を初期化
    unseis = []
    for sign in SIGNS:
        for blood in BLOODS:
            for zodiac in ZODIACS:
                unsei = Unsei(sign=sign, blood=blood, zodiac=zodiac)
                unseis.append(unsei)

    # rankingとrucky_itemを決定
    unseis = random.sample(unseis, len(unseis))
    for i in range(len(unseis)):
        unseis[i].rank = i + 1
        noun_index, adjective_index = rucky_item_indices[i]
        unseis[i].rucky_item = f'{adjectives[adjective_index]}{nouns[noun_index]}'

    # 出力
    output_txt = 'output.txt'
    with open(output_txt, 'w') as f:
        for unsei in unseis:
            res = f'{repr(unsei)}'
            f.write(res)

