from uranai import _read_txt, _write_txt
import datetime
from pathlib import Path


README_TITLE = '# uranai-forecast'
NEW_LINE = '\n'


if __name__ == '__main__':
    
    # 本日を取得
    d = datetime.datetime.now().strftime('%Y年%m月%d日')
    today_txt = f'{d}の運勢ランキングTOP10\n'

    # output.txtを読み込み10位までの運勢を取得
    results = []
    output_txt_path = Path('output.txt')
    for i, row in enumerate(_read_txt(output_txt_path)):
        if i == 10:
            continue
        results.append(row)

    # README.mdに更新情報を書き込み
    readme_md_path = Path('README.md')
    rows = []
    rows.append(README_TITLE)
    for i in range(2):
        rows.append(NEW_LINE)
    rows.append(today_txt)
    rows += results
    _write_txt(readme_md_path, rows)

