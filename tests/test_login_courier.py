import allure
import requests

from data import  TestEndpoint
from helper import register_new_courier_and_return_login_password
from helper import  generate_random_string


class TestLoginCourier():

    @allure.title('Проверка успешной авторизации курьера')
    @allure.title('Отправка запроса на авторизацию зарегистрированного курьера')
    def test_authorization_courier_all_valid_data_success(self):
        login_pass = register_new_courier_and_return_login_password()

        payload = {
            "login": login_pass[0],
            "password": login_pass[1]
        }

        response = requests.post(TestEndpoint.endpoint_login_courier, data = payload )

        assert response.status_code == 200 and response.json()["id"] > 0

    @allure.title('Проверка авторизации курьера с невалидным логином')
    @allure.description('Отправка запроса на авторизацию курьера с несуществующим логином')
    def test_authorization_courier_nonexisted_login_shows_error(self):
        login_nonexisted = generate_random_string(15)
        login_pass = register_new_courier_and_return_login_password()

        payload = {
            "login": login_nonexisted,
            "password": login_pass[1]
        }

        response = requests.post(TestEndpoint.endpoint_login_courier, data=payload)

        assert  response.status_code == 404 and response.json()["message"] == 'Учетная запись не найдена'


    @allure.title('Проверка авторизации курьера с невалидным паролем')
    @allure.description('Отправка запроса на авторизацию курьера с несуществующим паролем')
    def test_authorization_courier_nonexisted_password_shows_error(self):
        password_nonexisted = generate_random_string(15)
        login_pass = register_new_courier_and_return_login_password()

        payload = {
            "login": login_pass[0],
            "password": password_nonexisted
        }

        response = requests.post(TestEndpoint.endpoint_login_courier, data=payload)

        assert response.status_code == 404 and response.json()["message"] == 'Учетная запись не найдена'

    @allure.title('Проверка авторизации курьера с ошибкой в логине')
    @allure.description('Отправка запроса на авторизацию курьера при отсутствии поля логин')
    def test_authorization_courier_missing_login_field_shows_error(self):
        password = generate_random_string(10)

        payload = {
            "password": password
        }

        response = requests.post(TestEndpoint.endpoint_login_courier, data=payload)

        assert response.status_code == 400 and response.json()["message"] == 'Недостаточно данных для входа'

    @allure.title('Проверка авторизации курьера с ошибкой в пароле')
    @allure.description('Отправка запроса на авторизацию курьера при отсутствии поля пароль')
    def test_authorization_courier_missing_password_field_shows_error(self):
        login = generate_random_string(10)

        payload = {
            "login": login
        }

        response = requests.post(TestEndpoint.endpoint_login_courier, data=payload)

        assert response.status_code == 400 and response.json()["message"] == 'Недостаточно данных для входа'


