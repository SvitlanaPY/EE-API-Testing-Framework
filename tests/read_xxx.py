import json

def read_data_from_file(file_name):
    my_tuples = []
    try:
        with open(file_name, 'r') as f:
            # Зчитуємо дані JSON
            data_list = json.load(f)
            # Перетворюємо кожен список у кортеж
            # my_tuples = [tuple(item) for item in data_list]
            for item in data_list:
                my_tuples.append(tuple(item))
        return my_tuples
    except FileNotFoundError:
        assert False, f"Файл '{file_name}' не знайдено."
    except json.JSONDecodeError as e:
        assert False, f"Помилка декодування JSON у файлі '{file_name}': {e}. Перевірте формат JSON."
    except Exception as e:
        assert False, f"Виникла невідома помилка: {e}"

print(read_data_from_file('xxx.json'))
# [('https://fd.staging.inscyth.com/api/stores', '07450', 6), ('https://lowes.staging.inscyth.com/api/stores', '07450', 5)]

