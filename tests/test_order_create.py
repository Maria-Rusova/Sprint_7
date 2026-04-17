import pytest
import allure
from conftest import attach_response_to_allure
from helpers.faker_data import generate_order_payload
from helpers.api_client import ApiClient
from helpers.api_constants import ApiData


@allure.suite('Тесты создания заказов')
class TestOrderCreation:
    @allure.title('Создание заказа с разными цветами')
    @pytest.mark.parametrize('color', [
        ApiData.COLORS_BLACK,
        ApiData.COLORS_GREY,
        ApiData.COLORS_MIXED,
        ApiData.COLORS_EMPTY
    ])

    def test_create_order_with_color(self, color):
        payload = generate_order_payload(color=color)       
        response = ApiClient.create_order(payload)
        attach_response_to_allure(response)
        response_json = response.json()
        assert response.status_code == ApiData.HTTP_STATUS_CREATED
        assert ApiData.RESP_FIELD_TRACK in response_json

