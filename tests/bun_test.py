import pytest
from praktikum.bun import Bun


class TestBun:
    def test_bun_get_name(self):
        bun = Bun("Чёрная булка", 100)
        name = bun.get_name()
        assert name == "Чёрная булка"

    def test_bun_get_price(self):
        bun = Bun("Белая булка", 200)
        price = bun.get_price()
        assert price == 200

    def test_bun_constructor(self):
        bun = Bun("Красная булка", 300)
        assert (bun.name, bun.price) == ("Красная булка", 300)
