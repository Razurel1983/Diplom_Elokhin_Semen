import requests_function


def test_track_order():
    track_number = requests_function.post_new_order()
    get_response = requests_function.get_order(track_number.json()["track"])
    assert get_response.status_code == 200


# Семён Елохин, 11-я когорта – Дипломный проект. Инженер по тестированию Плюс