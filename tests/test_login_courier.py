import allure
from conftest import attach_response_to_allure
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
        attach_response_to_allure(response)    
        assert response.status_code == ApiData.HTTP_STATUS_OK
        assert 'id' in response_json, "В ответе отсутствует поле 'id'" # ответ пришел, проверку можно расширить"
        assert response_json['id'] is not None, "Поле 'id' имеет значение None" 

    @allure.title('Ошибка при неверном/несуществующем пароле')
    def test_login_fail_pass(self, created_courier):
        response = ApiClient.login_courier({'login' : created_courier['login'], 'password' : 'lolipops'})
        attach_response_to_allure(response)
        response_json = response.json()
        assert response.status_code == ApiData.HTTP_STATUS_NOT_FOUND
        assert response_json['message'] == ApiData.ERROR_ACCOUNT_NOT_FOUND

    @allure.title('Ошибка при отсутствии логина')
    def test_login_missing(self):
        response = ApiClient.login_courier({'password' : '123'})
        attach_response_to_allure(response)
        response_json = response.json()
        assert response.status_code == ApiData.HTTP_STATUS_BAD_REQUEST
        assert response_json['message'] == ApiData.ERROR_MISSING_DATA

    @allure.title('Ошибка авторизации несуществующего пользователя')
    def test_login_not_exist(self):
        response = ApiClient.login_courier({'login' : 'laize', 'password' : '123123'})
        attach_response_to_allure(response)
        response_json = response.json()
        assert response.status_code == ApiData.HTTP_STATUS_NOT_FOUND
        assert response_json['message'] == ApiData.ERROR_ACCOUNT_NOT_FOUND