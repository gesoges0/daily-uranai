import datetime
from pathlib import Path

from attribute import Eto, Ketsuekigata, Seiza
from utils import read_tsv, japanese_d, write_txt, YYYYmmdd

README_TITLE: str = "# daily-uranai"
NEW_LINE: str = "\n"
TABLE_HEADER: str = "|順位|血液型|星座|干支|ラッキーアイテム|"
TABLE_HR: str = "|-----------|-----------|-----------|-----------|-----------|"
RANKING_TITLE: str = "#### 全順位"
RANKING_ADVISE: str = "Ctrl+Fで検索してね"
TABLE_HR_FOR_RANKING: str = "|-----------|-----------|-----------|"

if __name__ == "__main__":

    # info
    ranking_tsv: Path = Path(f"output/ranking_{YYYYmmdd}.tsv")

    # get today
    TOP: int = 3
    TABLE_TITLE: str = f"### {japanese_d}の運勢ランキングTOP{TOP}"

    # read output.txt and store best 3 to list
    best3: list[list[str]] = [
        unsei_info for unsei_info in list(read_tsv(ranking_tsv))[:TOP]
    ]

    # arrange output
    readme_txts: list[str] = [
        README_TITLE + NEW_LINE,
        NEW_LINE,
    ]

    table_txts: list[str] = [
        TABLE_TITLE + NEW_LINE,
        TABLE_HEADER + NEW_LINE,
        TABLE_HR + NEW_LINE,
    ]

    table_rows: list[str] = [
        f"|{best[0]}|{best[5]}|{best[6]}|{best[7]}|{best[4]}|{NEW_LINE}"
        for best in best3
    ]

    table_txts += table_rows

    readme_txts += table_txts

    readme_txts += [NEW_LINE]

    ranking_txts: list[str] = [
        RANKING_TITLE + NEW_LINE,
        RANKING_ADVISE + NEW_LINE,
        TABLE_HR_FOR_RANKING + NEW_LINE,
    ]

    rankings: list[str] = [
        f"|{ranking[0]}|{ranking[1]}x{ranking[2]}x{ranking[3]}|{ranking[4]}|{NEW_LINE}"
        for ranking in read_tsv(ranking_tsv)
    ]

    ranking_txts += rankings

    readme_txts += ranking_txts

    write_txt(Path("README2.md"), readme_txts)

