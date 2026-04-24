from faker import Faker

fake_ru = Faker('ru_RU')
fake_en = Faker('en_US')


def generate_login():
    return fake_en.user_name() + str(fake_en.random_number(digits = 4))

def generate_password():
    return fake_en.password(
        length = 10,
        special_chars = False,
        digits = True,
        upper_case = False
    )

def generate_first_name():
    return fake_ru.first_name()

def generate_last_name():
    return fake_ru.last_name()

def generate_address():
    return fake_ru.street_address()

def generate_metro_st():
    return fake_ru.random_int(min = 1, max = 150)

def generate_phone_num():
    return fake_ru.phone_number()

def generate_rent_time():
    return fake_ru.random_int(min = 1, max = 10)

def generate_delivery_date():
    return str(fake_ru.future_date(end_date = '+31d'))

def generate_comment():
    return fake_ru.text(50)

def generate_courier_data():
    return {
        'login': generate_login(),
        'password': generate_password(),
        'first_name': generate_first_name()
    }

def generate_order_payload(color=None):
    return {
        'first_name': generate_first_name(),
        'last_name': generate_last_name(),
        'address': generate_address(),
        'metroSt': generate_metro_st(),
        'phone': generate_phone_num(),
        'rentTime': generate_rent_time(),
        'deliveryDate': generate_delivery_date(),
        'comment': generate_comment(),
        'color': color
    }