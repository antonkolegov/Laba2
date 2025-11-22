import re
from typing import List

def is_valid_date_format(date_str: str) -> bool:
    """Проверяет синтаксис даты ДД.ММ.ГГГГ."""
    pattern = r'^(0[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[0-2])\.(1[0-9]{3}|2[0-9]{3})$'
    return bool(re.fullmatch(pattern, date_str))

def find_dates_in_text(text: str) -> List[str]:
    """Ищет все даты ДД.ММ.ГГГГ в тексте."""
    pattern = r'\b(0[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[0-2])\.(1[0-9]{3}|2[0-9]{3})\b'
    matches = re.findall(pattern, text)
    return [f"{d}.{m}.{y}" for d, m, y in matches]

def find_dates_in_file(filename: str) -> List[str]:
    """Читает файл и возвращает все найденные даты."""
    with open(filename, 'r', encoding='utf-8') as f:
        return find_dates_in_text(f.read())

if __name__ == '__main__':
    print("=== Поиск дат в input.txt ===")
    try:
        dates = find_dates_in_file('input.txt')
        for i, d in enumerate(dates, 1):
            print(f"{i:2}. {d}")
    except FileNotFoundError:
        print("Файл input.txt не найден.")