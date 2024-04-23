import configuration
import data
import requests


def create_order(create_order):
    return requests.post(
        configuration.URL_SERVICE + configuration.PATH_CREATE_ORDER,
        json=create_order,
        headers=data.headers,
    )


# Получение заказа по треку
def get_order_track(track_order):
    return requests.get(
        configuration.URL_SERVICE + configuration.PATH_GET_TRACK,
        params={"t": track_order},
    )
