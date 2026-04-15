import allure
from conftest import ara
from helpers.api_client import ApiClient
from helpers.api_constants import ApiData


@allure.suite('Тесты авторизации курьера')
class TestCourierLogin:
    @allure.title('Успешная авторизация курьера')
    def test_login_succ(self, created_courier):
        login = created_courier['login']
        password = created_courier['password']
        response = ApiClient.login_courier({'login' : login, 'password' : password})
        response_json = response.json()
        ara(response)    
        assert response.status_code == ApiData.HTTP_STATUS_OK
        assert 'id' in str(response_json)      

    @allure.title('Ошибка при неверном/несуществующем пароле')
    def test_login_fail_pass(self, created_courier):
        response = ApiClient.login_courier({'login' : created_courier['login'], 'password' : 'lolipops'})
        ara(response)
        response_json = response.json()
        assert response.status_code == ApiData.HTTP_STATUS_NOT_FOUND
        assert ApiData.ERROR_ACCOUNT_NOT_FOUND in str(response_json)

    @allure.title('Ошибка при отсутствии логина')
    def test_login_missing(self):
        response = ApiClient.login_courier({'password' : '123'})
        ara(response)
        response_json = response.json()
        assert response.status_code == ApiData.HTTP_STATUS_BAD_REQUEST
        assert ApiData.ERROR_MISSING_DATA in str(response_json)

    @allure.title('Ошибка авторизации несуществующего пользователя')
    def test_login_not_exist(self):
        response = ApiClient.login_courier({'login' : 'laize', 'password' : '123123'})
        ara(response)
        response_json = response.json()
        assert response.status_code == ApiData.HTTP_STATUS_NOT_FOUND
        assert ApiData.ERROR_ACCOUNT_NOT_FOUND in str(response_json)