import pytest
import requests

from data import TestEndpoint, TestData
from helper import register_new_courier_and_return_login_password

#метод регистрирует и логинит курьера и возвращает id курьера
@pytest.fixture()
def id_courier():
    login_pass = register_new_courier_and_return_login_password()

    payload = {
        "login": login_pass[0],
        "password": login_pass[1]
    }

    response = requests.post(TestEndpoint.endpoint_login_courier, data=payload)
    yield response.json()['id']

    requests.delete(TestEndpoint.endpoint_delet_courier + str(response.json()['id']))



#метод создает заказ и возвращает его id по номеру трекa
@pytest.fixture()
def id_order():
    response = requests.post(TestEndpoint.endpoint_order, json=TestData.order_data_color_black)
    track = response.json()['track']

    response = requests.get(TestEndpoint.endpoint_receipt_order_by_track, params={'t': track})
    yield response.json()['order']['id']

    requests.delete(TestEndpoint.endpoint_delet_order, json = {'track': response.json()['order']['track']})

