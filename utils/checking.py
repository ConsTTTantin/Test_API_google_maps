import json
from utils.api import GoogleMapsApi
import requests

"""Методы для проверки наших запросов"""

class Checking():

    """Метод для проверки статус кода"""
    @staticmethod
    def check_status_code(result, status_code):
        assert status_code == result.status_code
        print(f"УСПЕШНО, Статус код: {result.status_code}")


    """Метод для проверки обязательных полей в ответе запроса"""
    @staticmethod
    def check_json_key(result, expected_value):
        check = result.json()
        assert list(check) == expected_value
        print("Все поля присутствуют")


    """Метод для проверки значений обязательных полей в ответе запроса"""
    @staticmethod
    def check_json_value(result, field_name, expected_value):
        check = result.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print(f"{field_name} верен!")