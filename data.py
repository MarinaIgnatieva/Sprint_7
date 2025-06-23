class TestEndpoint():

    url_scooter = "https://qa-scooter.praktikum-services.ru"
    endpoint_add_courier = f"{url_scooter}/api/v1/courier"
    endpoint_login_courier = f"{url_scooter}/api/v1/courier/login"
    endpoint_order = f"{url_scooter}/api/v1/orders"
    endpoint_delet_courier = f"{url_scooter}/api/v1/courier/"
    endpoint_receipt_order_by_track = f"{url_scooter}/api/v1/orders/track"
    endpoint_accept_order = f"{url_scooter}/api/v1/orders/accept/"
    endpoint_delet_order = f"{url_scooter}/api/v1/orders/cancel/"

class TestData():



    order_data_color_black = {
            "firstname": "Иван",
            "lastName": "Иванов",
            "address": "Москва, ул. Тверская, 1",
            "metro": "Лубянка",
            "phone": "89998887766",
            "rentTime": 5,
            "deliveryDate": "2025-12-22",
            "comment": "Позвонить за час",
            "color": [
                "BLACK"
            ]
        }



    order_data_color_grey = {
            "firstname": "Иван",
            "lastName": "Иванов",
            "address": "Москва, ул. Тверская, 1",
            "metro": "Лубянка",
            "phone": "89998887766",
            "rentTime": 5,
            "deliveryDate": "2025-12-22",
            "comment": "Позвонить за час",
            "color": [
                "GREY"
            ]
        }

    order_data_color_black_and_grey = {
            "firstname": "Иван",
            "lastName": "Иванов",
            "address": "Москва, ул. Тверская, 1",
            "metro": "Лубянка",
            "phone": "89998887766",
            "rentTime": 5,
            "deliveryDate": "2025-12-22",
            "comment": "Позвонить за час",
            "color": [
                "BLACK",
                "GREY"
            ]
        }

    order_data_none_color = {
            "firstname": "Иван",
            "lastName": "Иванов",
            "address": "Москва, ул. Тверская, 1",
            "metro": "Лубянка",
            "phone": "89998887766",
            "rentTime": 5,
            "deliveryDate": "2025-12-22",
            "comment": "Позвонить за час",
            "color": []
        }

