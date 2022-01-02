"""
You are given the following code:

class Order:
    morning_discount = 0.25

    def __init__(self, price):
        self.price = price

    def final_price(self):
        return self.price - self.price * self.morning_discount

Make it possible to use different discount programs.
Hint: use strategy behavioural OOP pattern.
https://refactoring.guru/design-patterns/strategy

Example of the result call:

def morning_discount(order):
    ...

def elder_discount(order):
    ...

order_1 = Order(100, morning_discount)
assert order_1.final_price() == 75

order_2 = Order(100, elder_discount)
assert order_2.final_price() == 10
"""


class DiscountStrategy:
    """
    Class that defines the amount of discount
    depending on daytime.

    :param strategy: daytime
    :type strategy: str
    """
    def __init__(self, strategy: str):
        self.discount = .0
        if strategy == 'morning':
            self.discount = .25
        elif strategy == 'evening':
            self.discount = .75


class Order:
    """
    An order with its price and discount.

    :param price: order's cost
    :type price: float
    :param discount: the type of discount
    :type discount: DiscountStrategy
    """
    def __init__(self, price, discount: DiscountStrategy):
        self.price = price
        self.discount = discount.discount

    def final_price(self):
        return self.price - self.price * self.discount


if __name__ == '__main__':
    morning_discount = DiscountStrategy('morning')
    order_1 = Order(100, morning_discount)
    print(order_1.final_price())
    evening_discount = DiscountStrategy('evening')
    order_2 = Order(100, evening_discount)
    print(order_2.final_price())
