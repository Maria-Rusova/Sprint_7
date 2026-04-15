import allure
import pytest
from conftest import ara
from helpers.faker_data import generate_courier_data
from helpers.api_client import ApiClient
from helpers.api_constants import ApiData


@allure.suite('Тесты создания курьера')
class TestCourierCreation:
    @allure.title('создание курьера')    
    def test_create_courier_succ(self):
        payload = generate_courier_data()
        response = ApiClient.create_courier(payload)
        ara(response)
        response_json = response.json()
        assert response.status_code == ApiData.HTTP_STATUS_CREATED
        assert response_json == ApiData.RESP_OK   

    @allure.title('нельзя создать двух одинаковых курьеров')
    def test_create_courier_dubl_fail(self, created_courier):
        payload = created_courier['payload']
        response = ApiClient.create_courier(payload)
        ara(response)
        response_json = response.json()
        assert response.status_code == ApiData.HTTP_STATUS_CONFLICT
        assert ApiData.ERROR_LOGIN_ALREADY_USED in str(response_json)

    @allure.title('нельзя создать курьера без логина или без пароля')
    @pytest.mark.parametrize('payload', ApiData.ERROR_COURIER_CREATION)
    def test_create_courier_incomplete_data(self, payload):
        response = ApiClient.create_courier(payload)
        ara(response)
        response_json = response.json()
        assert response.status_code == ApiData.HTTP_STATUS_BAD_REQUEST
        assert ApiData.ERROR_INSUFFICIENT_DATA in str(response_json)