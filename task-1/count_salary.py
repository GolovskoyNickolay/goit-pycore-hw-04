import os.path


def total_salary(path: str) -> tuple[int, int]:
    check_file = os.path.isfile(path)
    if check_file:
        with open(path, encoding='utf-8') as salary_file:
            try:
                lines = salary_file.readlines()
                total_count = 0
                for line in lines:
                    total_count += int(line.split(',')[1].strip())
                return total_count, total_count // len(lines)
            except Exception:
                print('Could not parse salary file.')
                return 0, 0
    else:
        print('File not found')
        return 0, 0


total, average = total_salary("salary.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
