import json

def read_data_from_file(file_name):
    try:
        with open(file_name, 'r') as f:
            # Зчитуємо дані JSON
            data_list = json.load(f)
        return data_list
    except FileNotFoundError:
        assert False, f"Файл '{file_name}' не знайдено."
    except json.JSONDecodeError as e:
        assert False, f"Помилка декодування JSON у файлі '{file_name}': {e}. Перевірте формат JSON."
    except Exception as e:
        assert False, f"Виникла невідома помилка: {e}"

print(read_data_from_file('data_test_stores.json'))
# {'storesMaxQty_Parameters': [['https://fd.staging.inscyth.com/api/stores', '07450', 6], ['https://lowes.staging.inscyth.com/api/stores', '07450', 5]], 'storesQty_byStoreId_Parameters': [['https://fd.staging.inscyth.com/api/stores', '07450', 22788]]}

