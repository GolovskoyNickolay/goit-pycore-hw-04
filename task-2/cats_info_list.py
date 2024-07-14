import os.path
from typing import Dict


def get_cats_info(path: str) -> list[Dict[str, str]]:
    check_file = os.path.isfile(path)
    if check_file:
        with open(path, encoding='utf-8') as salary_file:
            try:
                lines = salary_file.readlines()
                list_of_cats_info = []
                for line in lines:
                    splitted_line = line.strip().split(',')
                    list_of_cats_info.append({
                        'id': splitted_line[0],
                        'name': splitted_line[1],
                        'age': splitted_line[2],
                    })
                return list_of_cats_info
            except Exception:
                print('Could not parse salary file.')
                return []
    else:
        print('File not found')
        return []


cats_info = get_cats_info("cats.txt")
print(cats_info)
