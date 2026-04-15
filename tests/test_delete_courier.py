import allure
from conftest import ara
from helpers.api_client import ApiClient
from helpers.api_constants import ApiData


@allure.suite('Тесты удаления курьера')
class TestCourierDeletion:

    @allure.title('Успешное удаление курьера')
    def test_delete_courier_success(self, created_courier):
        courier_id = created_courier['id']
        response = ApiClient.delete_courier(courier_id)
        ara(response)
        response_json = response.json()
        assert response.status_code == ApiData.HTTP_STATUS_OK
        assert response_json == ApiData.RESP_OK