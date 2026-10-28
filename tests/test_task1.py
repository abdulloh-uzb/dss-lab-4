from task1 import Cart
import pytest


def test_cart():
    cart1 = Cart(user_id=1)
    cart2 = Cart(user_id=2)

    cart1.add('sku1', 2)
    cart1.add('sku2', 1)

    assert len(cart2.items) == 0

