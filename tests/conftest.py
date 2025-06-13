import pytest
import requests
import json

@pytest.fixture(scope="session")
def test_data():
    # def read_data_from_file():
    file_name = "data_test_stores.json"
    try:
        with open(file_name, 'r') as f:
            # Зчитуємо дані JSON
            data = json.load(f)
        return data
    except FileNotFoundError:
        assert False, f"Файл '{file_name}' не знайдено."
    except json.JSONDecodeError as e:
        assert False, f"Помилка декодування JSON у файлі '{file_name}': {e}. Перевірте формат JSON."
    except Exception as e:
        assert False, f"Виникла невідома помилка: {e}"


