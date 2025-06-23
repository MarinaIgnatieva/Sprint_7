import allure
import pytest
import requests

from data import TestEndpoint



class TestDeletCourier():

    @allure.title('Проверка успешного удаления курьера')
    def test_delet_curier_success(self, id_courier):
        response = requests.delete(TestEndpoint.endpoint_delet_courier + str(id_courier))

        assert response.status_code == 200 and response.json()["ok"]



    @allure.title('Проверка возвращения ошибки при отправке запроса на удаление курьера без указания id курьера')
    def test_delet_courier_visout_id_shows_error(self):
        response = requests.delete(TestEndpoint.endpoint_delet_courier)

        assert response.status_code == 400 and response.json()['message'] == "Недостаточно данных для удаления курьера"



    @allure.title('Проверка возвращения ошибки при отправке запроса на удаление курьера с указанием '
                  'несуществующего id курьера')
    def test_delet_courier_nonexisted_id_shows_error(self):
        response = requests.delete(TestEndpoint.endpoint_delet_courier + '1000000000')

        assert response.status_code == 404 and response.json()['message'] == "Курьера с таким id нет."

