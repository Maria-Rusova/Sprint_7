from helpers.faker_data import *

class ApiData:

    # Ожидаемые тела ответов
    RESP_OK = {'ok': True}
    RESP_FIELD_TRACK = 'track'

    # HTTP-статусы
    HTTP_STATUS_CREATED = 201
    HTTP_STATUS_CONFLICT = 409
    HTTP_STATUS_OK = 200
    HTTP_STATUS_NOT_FOUND = 404
    HTTP_STATUS_BAD_REQUEST = 400

    # Сообщения об ошибках
    ERROR_LOGIN_ALREADY_USED = 'Этот логин уже используется. Попробуйте другой.'
    ERROR_ACCOUNT_NOT_FOUND = 'Учетная запись не найдена'
    ERROR_MISSING_DATA = 'Недостаточно данных для входа'
    ERROR_INSUFFICIENT_DATA = "Недостаточно данных для создания учетной записи"

    # Цвета для заказов
    COLORS_BLACK = ['BLACK']
    COLORS_GREY = ['GREY']
    COLORS_MIXED = ['BLACK', 'GREY']
    COLORS_EMPTY = []

    # Наборы тестовых данных для ошибок создания курьера
    ERROR_COURIER_CREATION = [
        (
            {'password': generate_password(), 'first_name': generate_first_name()}
        ),
        (
            {'login': generate_login(), 'first_name': generate_first_name()}
        )
    ]