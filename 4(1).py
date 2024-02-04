def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            total_salary = 0
            num_developers = 0
            for line in lines:
                name, salary = line.strip().split(',')
                total_salary += int(salary)
                num_developers += 1
            if num_developers == 0:
                raise ValueError("Файл порожній. Немає даних про розробників.")
            average_salary = total_salary / num_developers
            return total_salary, average_salary
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл '{path}' не знайдено.")
    except Exception as e:
        raise Exception(f"Помилка при обробці файлу: {str(e)}")

try:
    total, average = total_salary("path/to/salary_file.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
except Exception as e:
    print(f"Помилка: {str(e)}")
