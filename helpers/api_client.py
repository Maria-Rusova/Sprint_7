import allure
import requests
from helpers.urls import Urls


class ApiClient:
    @staticmethod
    @allure.step("Создание курьера")
    def create_courier(payload):
        return requests.post(Urls.COURIER_ENDPOINT, data=payload)

    @staticmethod
    @allure.step("Авторизация курьера")
    def login_courier(payload):
        return requests.post(Urls.LOGIN_ENDPOINT, data=payload)

    @staticmethod
    @allure.step("Создание заказа")
    def create_order(payload):
        return requests.post(Urls.ORDERS_ENDPOINT, json=payload)

    @staticmethod
    @allure.step("Получение списка заказов")
    def get_orders():
        return requests.get(Urls.ORDERS_ENDPOINT)
    
    @staticmethod
    @allure.step("Удаление курьера")
    def delete_courier(courier_id):
        return requests.delete(f"{Urls.COURIER_ENDPOINT}/{courier_id}")