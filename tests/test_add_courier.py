import allure
import pytest
import requests

from data import TestEndpoint
from helper import generate_random_string


class TestAddCourier:

    @allure.title('Успешное создание курьера')
    @allure.description('Отправка запроса на регистрацию нового курьера')
    def test_add_courier_all_valid_data_success(self):
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        response = requests.post(TestEndpoint.endpoint_add_courier, data=payload)

        assert response.status_code == 201 and response.json()["ok"]

    @allure.title('Проверка создания двух одинаковых курьеров')
    @allure.description('Отправка запроса на регистрацию двух курьеров с одинаковыми логином, паролем и именем')
    def test_add_duplicate_courier_shows_error(self):
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        requests.post(TestEndpoint.endpoint_add_courier, data=payload)

        response = requests.post(TestEndpoint.endpoint_add_courier, data=payload)

        assert response.status_code == 409 and response.json()['message'] == "Этот логин уже используется. Попробуйте другой."

    @allure.title('Проверка создания курьера с невалидными данными')
    @allure.description('Отправка запроса на регистрацию курьера без указания имени; без указания пароля; без указания логина')
    @pytest.mark.parametrize('payload', [
        [{'login':generate_random_string(10), 'password':generate_random_string(10)}],
        [{'login':generate_random_string(10), 'firstName':generate_random_string(10)}],
        [{'password':generate_random_string(10), 'firstName':generate_random_string(10)}]
    ])
    def test_add_courier_missing_field_shows_error(self, payload):
        response = requests.post(TestEndpoint.endpoint_add_courier, data=payload)

        assert response.status_code == 400 and response.json()['message'] == "Недостаточно данных для создания учетной записи"