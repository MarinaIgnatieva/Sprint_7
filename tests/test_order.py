import pytest
import requests
import allure

from data import TestEndpoint
from data import TestData



class TestOrder():

    @allure.title('Проверка успешного создания заказа')
    @allure.description('Отправка запроса на создание заказа с выбором цвета самоката: черный; серый; '
                        'черный и серый; без указания цвета')
    @pytest.mark.parametrize('data',[
        TestData.order_data_color_black,
        TestData.order_data_color_grey,
        TestData.order_data_color_black_and_grey,
        TestData.order_data_none_color
    ] )
    def test_order_choice_color_scooter_success(self, data):
        response = requests.post(TestEndpoint.endpoint_order,  json=data)

        assert response.status_code == 201 and "track" in response.text



class TestListOrder():

    @allure.title('Проверка получения списка заказов')
    def test_list_order_success(self):
        response = requests.get(TestEndpoint.endpoint_order)

        assert response.status_code == 200 and len(response.json()['orders']) > 0


class TestAcceptOrder():

    @allure.title('Проверка успешного принятия заказа')
    @allure.description('Отправка запроса на принятие заказа с указанием существующего id курьера и'
                        'существующего id заказа')
    def test_accept_order_success(self, id_courier, id_order ):
        response = requests.put(TestEndpoint.endpoint_accept_order + str(id_order), params={'courierId':id_courier})

        assert response.status_code == 200 and response.json()['ok']



    @allure.title('Проверка возвращения ошибки при принятия заказа без указания id курьера')
    def test_accept_order_missing_id_courier_shows_error(self, id_order):
        response = requests.put(TestEndpoint.endpoint_accept_order + str(id_order))

        assert response.status_code == 400 and response.json()['message'] == "Недостаточно данных для поиска"



    @allure.title('Проверка возвращения ошибки при принятия заказа с указанием несуществующего id курьера')
    def test_accept_order_nonexisted_id_courier_shows_error(self, id_order):
        response = requests.put(TestEndpoint.endpoint_accept_order + str(id_order), params={'courierId': 1000000000})

        assert response.status_code == 404 and response.json()['message'] == "Курьера с таким id не существует"



    @allure.title('Проверка возвращения ошибки при принятия заказа без указания id заказа')
    def test_accept_order_missing_id_order_shows_error(self, id_courier):
        response = requests.put(TestEndpoint.endpoint_accept_order, params={'courierId': id_courier})

        assert response.status_code == 400 and response.json()['message'] == "Недостаточно данных для поиска"



    @allure.title('Проверка возвращения ошибки при принятия заказа с указанием несуществующего id заказа')
    def test_accept_order_nonexisted_id_order_shows_error(self, id_courier):
        response = requests.put(TestEndpoint.endpoint_accept_order + str(1000000000), params={'courierId': id_courier})

        assert response.status_code == 404 and response.json()['message'] == "Заказа с таким id не существует"



class TestReceiptOrder():

    @allure.title('Проверка успешного получения заказа по его номеру')
    def test_receipt_order_by_track_success(self):
        response = requests.post(TestEndpoint.endpoint_order, json=TestData.order_data_color_black)
        track = response.json()['track']

        response = requests.get(TestEndpoint.endpoint_receipt_order_by_track, params={'t': track})

        assert response.status_code == 200 and response.json()['order']['id'] > 0



    @allure.title('Проверка возвращения ошибки при получении заказа с указанием несуществующего номера заказа')
    def test_receipt_order_by_nonexisted_track_shows_error(self):
        response = requests.get(TestEndpoint.endpoint_receipt_order_by_track, params={'t': 1000000000})

        assert response.status_code == 404 and response.json()['message'] == "Заказ не найден"



    @allure.title('Проверка возвращения ошибки при получении заказа без указания номера заказа')
    def test_receipt_order_by_missing_track_shows_error(self):
        response = requests.get(TestEndpoint.endpoint_receipt_order_by_track)

        assert response.status_code == 400 and response.json()['message'] == "Недостаточно данных для поиска"