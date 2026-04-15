import allure
from conftest import ara
from helpers.api_client import ApiClient
from helpers.api_constants import ApiData


@allure.suite('Тесты работы со списком заказов')
class TestOrdersList:
    @allure.title('Возвращение списка заказов')
    def test_get_orders_list(self):
        response = ApiClient.get_orders()
        data = response.json()
        ara(response)
        response_json = response.json()
        assert response.status_code == ApiData.HTTP_STATUS_OK
        assert isinstance(response_json['orders'], list)