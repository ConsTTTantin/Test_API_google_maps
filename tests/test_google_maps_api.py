import allure

from utils.api import GoogleMapsApi
from utils.checking import Checking


"""Создание, запроси, изменение и удаление новой локации"""

@allure.epic("Тест новой локации")
class TestCreatePlace():

    @allure.description("Создание, обновление, удаление и проверка локации")
    def test_create_new_place(self):
        print("\nМетод POST")
        result_post = GoogleMapsApi.craete_new_place()
        check_post = result_post.json()
        place_id = check_post.get("place_id")
        Checking.check_status_code(result_post, 200)
        Checking.check_json_key(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        Checking.check_json_value(result_post, "status", "OK")

        print("\nМетод GET POST")
        result_get = GoogleMapsApi.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_key(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        Checking.check_json_value(result_get, "address", "29, side layout, cohen 09")

        print("\nМетод PUT")
        result_put = GoogleMapsApi.put_new_place(place_id)
        Checking.check_status_code(result_put, 200)
        Checking.check_json_key(result_put, ['msg'])
        Checking.check_json_value(result_put, 'msg', "Address successfully updated")

        print("\nМетод GET PUT")
        result_get = GoogleMapsApi.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_key(result_get,
                                ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        Checking.check_json_value(result_get, "address", "Dmitrovsokoe schose 100")

        print("\nМетод DELETE")
        result_delete = GoogleMapsApi.delete_place(place_id)
        Checking.check_status_code(result_delete, 200)
        Checking.check_json_key(result_delete, ['status'])
        Checking.check_json_value(result_delete, "status", "OK")

        print("\nМетод GET DELETE")
        result_get = GoogleMapsApi.get_new_place(place_id)
        Checking.check_status_code(result_get, 404)
        Checking.check_json_key(result_get, ['msg'])
        Checking.check_json_value(result_get, "msg", "Get operation failed, looks like place_id  doesn't exists")

        print("\nТестирование по Google Maps прошло успешно")
