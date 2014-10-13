# Storing amounts of currency in floats is a bad, bad idea. Therefore:
from decimal import Decimal
from collections import namedtuple
from functools import reduce

from gdp1.common.input_helpers import int_input

Product = namedtuple("Product", ["name", "price"])
OrderUnit = namedtuple("OrderUnit", ["name", "price", "amount"])


def main():
    print("The DIY Spot: For all your construction needs!")
    print()

    # We make the naive assumption that the plural of these words is formed by appending an "s".
    products = [
        Product("screw",     Decimal("0.07")),
        Product("screw nut", Decimal("0.04")),
        Product("grommet",   Decimal("0.02"))
    ]

    orders = []
    for product in products:
        amount = int_input("Please enter how many %ss you would like to order ($%.2f/piece): "
                           % (product.name, product.price)
                           )
        orders.append(OrderUnit(product.name, product.price, amount))

    total = reduce((lambda acc, order: acc + order.price * order.amount), orders, Decimal(0))

    print()
    print("You have ordered $%.2f worth of products." % total)


if __name__ == "__main__":
    main()
