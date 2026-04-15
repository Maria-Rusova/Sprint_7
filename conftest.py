import allure
import pytest
from helpers.faker_data import *
from helpers.api_client import ApiClient
from helpers.api_constants import ApiData


@pytest.fixture
def created_courier():
    with allure.step("Создание тестового курьера"):
        payload = generate_courier_data()
        create_response = ApiClient.create_courier(payload)
        assert create_response.status_code == ApiData.HTTP_STATUS_CREATED

        login_response = ApiClient.login_courier({
            'login': payload['login'],
            'password': payload['password']
        })
        assert login_response.status_code == ApiData.HTTP_STATUS_OK
        courier_id = login_response.json().get('id')

        courier_info = {
            'payload': payload,
            'id': courier_id,
            'login': payload['login'],
            'password': payload['password'],
            'first_name': payload['first_name']
        }

        allure.attach(
            body=str(courier_info),
            name="Данные созданного курьера",
            attachment_type=allure.attachment_type.JSON
        )
    yield courier_info

    with allure.step("Очистка данных: курьер удалён"):
        if courier_info['id'] is not None:
            delete_response = ApiClient.delete_courier(courier_info['id'])
            
            allure.attach(
                body=f"ID курьера: {courier_info['id']}",
                name="Удаляемый курьер",
                attachment_type=allure.attachment_type.TEXT
            )
            allure.attach(
                body=delete_response.text,
                name="Ответ сервера при удалении",
                attachment_type=allure.attachment_type.TEXT
            )
            allure.attach(
                body=str(delete_response.status_code),
                name="Статус-код при удалении",
                attachment_type=allure.attachment_type.TEXT
            )
        else:
            allure.attach(
                body="ID курьера не был получен, удаление пропущено",
                name="Статус очистки",
                attachment_type=allure.attachment_type.TEXT
            )

def ara (response): # attach response to allure
    with allure.step("Ответ сервера"):
        allure.attach(
            body=response.text,
            name="Тело ответа",
            attachment_type=allure.attachment_type.TEXT
        )
        allure.attach(
            body=str(response.status_code),
            name="Статус-код",
            attachment_type=allure.attachment_type.TEXT
        )