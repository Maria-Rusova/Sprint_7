import allure
from conftest import attach_response_to_allure
from helpers.api_client import ApiClient
from helpers.api_constants import ApiData


@allure.suite('Тесты работы со списком заказов')
class TestOrdersList:
    @allure.title('Возвращение списка заказов')
    def test_get_orders_list(self):
        response = ApiClient.get_orders()
        attach_response_to_allure(response)
        response_json = response.json()
        assert response.status_code == ApiData.HTTP_STATUS_OK
        assert isinstance(response_json['orders'], list)