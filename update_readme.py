from uranai import _read_txt, _write_txt
import datetime
from pathlib import Path
from attribute import Sign, Zodiac, Blood


README_TITLE = '# uranai-forecast'
NEW_LINE = '\n'


if __name__ == '__main__':
    
    # 本日を取得
    d = datetime.datetime.now().strftime('%Y年%m月%d日')
    today_txt = f'### {d}の運勢ランキングTOP10'

    # output.txtを読み込み10位までの運勢を取得
    results = []
    output_txt_path = Path('output.txt')
    for i, row in enumerate(_read_txt(output_txt_path)):
        if i == 10:
            break
        results.append(row)

    # 出力を整形
    new_rows = ['|順位|星座|干支|血液型|ラッキーアイテム|\n', '|-----------|-----------|-----------|-----------|-----------|\n']
    for i, result in enumerate(results):

        _  = result.split('\t')[1]
        racky_item = result.split('\t')[2]
        _sign, _zodiac, _blood = _.split(' x ')
        _sign = _sign.replace('座', '')
        _zodiac = _zodiac.replace('年', '')
        _blood = _blood.replace('型', '').upper()
        sign, zodiac, blood = Sign.get_sign_by_string(_sign), Zodiac.get_zodiac_by_string(_zodiac), Blood.get_blood_by_string(_blood)

        # PATHの形に整形
        row = f'|{i+1}位|{sign.path_gh}|{zodiac.path_gh}|{blood.path_gh}|{racky_item}|\n'
        new_rows.append(row)
        

    # README.mdに更新情報を書き込み
    readme_md_path = Path('README.md')
    rows = []
    rows.append(README_TITLE)
    for i in range(2):
        rows.append(NEW_LINE)
    rows.append(today_txt)
    rows.append(NEW_LINE)
    for row in new_rows:
        rows.append(row)
    
    # その他の順位も書き込み
    rows.append(NEW_LINE)
    rows.append('### 全順位\n')
    rows.append('|順位|星座x干支x血液型|ラッキーアイテム|\n')
    rows.append('|-----------|-----------|-----------|\n')
    for row in _read_txt(output_txt_path):
        rank, result, item = row.replace('\n', '').split('\t')
        rows.append(f'|{rank}|{result}|{item}|\n')

    _write_txt(readme_md_path, rows)

    
