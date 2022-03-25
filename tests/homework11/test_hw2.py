from homework11.hw2 import DiscountStrategy, Order


def test_order_with_discount():
    morning_discount = DiscountStrategy('morning')
    order_1 = Order(100, morning_discount)
    assert order_1.final_price() == 75

    evening_discount = DiscountStrategy('evening')
    order_2 = Order(100, evening_discount)
    assert order_2.final_price() == 25

    afternoon_discount = DiscountStrategy('afternoon')
    order_3 = Order(100, afternoon_discount)
    assert order_3.final_price() == 100
