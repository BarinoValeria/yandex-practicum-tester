import data
import sender


# Валерия Баринова, 15-я когорта — Финальный проект. Инженер по тестированию плюс
def positive_assert(track_order):
    order_response = sender.get_order_track(track_order)
    assert order_response.status_code == 200


def test_create_order_track_success():
    response = sender.create_order(data.create_order)
    track_order = response.json().get("track")
    positive_assert(track_order)
