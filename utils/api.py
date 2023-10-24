from utils.http_methods import HttpMethods

"""Методы для тестирования GoogleMapsApi"""

base_url = "https://rahulshettyacademy.com" # Базовый URL
key = "?key=qaclick123"   # Параметр для всех запросов

class GoogleMapsApi():

    """Метод для создания новой локации"""
    @staticmethod
    def craete_new_place():
        json_craete_new_place = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }
        post_resurse = "/maps/api/place/add/json"     # Ресурс метода POST
        post_url = f"{base_url}{post_resurse}{key}"
        print(post_url)
        result_post = HttpMethods.post(post_url, json_craete_new_place)
        print(result_post.json())
        return result_post


    """Метод для проверки новой локации"""
    @staticmethod
    def get_new_place(place_id):
        get_resurse = "/maps/api/place/get/json"      # Ресурс метода GET
        get_url = f"{base_url}{get_resurse}{key}&place_id={place_id}"
        print(get_url)
        result_get = HttpMethods.get(get_url)
        print(result_get.json())
        return result_get


    """Метод для изменения новой локации"""
    @staticmethod
    def put_new_place(place_id):
        put_resurse = "/maps/api/place/update/json"  # Ресурс метода PUT
        json_update_place = {
            "place_id": place_id,
            "address": "Dmitrovsokoe schose 100",
            "key": "qaclick123"
        }
        put_url = f"{base_url}{put_resurse}{key}"
        print(put_url)
        result_put = HttpMethods.put(put_url, json_update_place)
        print(result_put.json())
        return result_put

    """Метод для удаления локации"""
    @staticmethod
    def delete_place(place_id):
        del_resurse = "/maps/api/place/delete/json"    # Ресурс метода DELETE
        json_delete_place = {
            "place_id": place_id
        }
        delete_url = f"{base_url}{del_resurse}{key}"
        print(delete_url)
        result_delete = HttpMethods.delete(delete_url, json_delete_place)
        print(result_delete.json())
        return result_delete