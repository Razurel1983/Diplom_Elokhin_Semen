import requests
import configuration
import data


def post_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=data.order_body,
                         headers=data.headers)


def get_order(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER,
                        params={"t": track_number})