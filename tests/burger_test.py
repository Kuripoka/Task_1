import pytest
from praktikum.burger import Burger
from data import BUN_MOCK_NAME, BUN_MOCK_PRICE, INGREDIENT_MOCK_1, INGREDIENT_MOCK_2


class TestBurger:
    def test_burger_set_buns(self, bun_mock):
        burger = Burger()
        burger.set_buns(bun_mock)
        assert (burger.bun.name, burger.bun.price) == (BUN_MOCK_NAME, BUN_MOCK_PRICE)

    def test_burger_add_ingredient(self, ingredient_mock_1):
        burger = Burger()
        burger.add_ingredient(ingredient_mock_1)
        assert (burger.ingredients[0].name, burger.ingredients[0].price) == (INGREDIENT_MOCK_1["name"], INGREDIENT_MOCK_1["price"])

    def test_burger_remove_ingredient(self, ingredient_mock_1):
        burger = Burger()
        burger.add_ingredient(ingredient_mock_1)
        burger.add_ingredient(ingredient_mock_1)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1

    def test_burger_move_ingredient(self, ingredient_mock_1, ingredient_mock_2):
        burger = Burger()
        burger.add_ingredient(ingredient_mock_1)
        burger.add_ingredient(ingredient_mock_2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[1] is ingredient_mock_1

    def test_burger_get_price_with_multiple_ingredients(self, bun_mock, ingredient_mock_1, ingredient_mock_2):
        expected_price = BUN_MOCK_PRICE * 2 + INGREDIENT_MOCK_1["price"] + INGREDIENT_MOCK_2["price"]
        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_mock_1)
        burger.add_ingredient(ingredient_mock_2)
        assert burger.get_price() == expected_price

    def test_burger_get_receipt(self, bun_mock, ingredient_mock_1, ingredient_mock_2):
        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_mock_1)
        burger.add_ingredient(ingredient_mock_2)
        expected_price = BUN_MOCK_PRICE * 2 + INGREDIENT_MOCK_1["price"] + INGREDIENT_MOCK_2["price"]
        receipt = burger.get_receipt()
        assert BUN_MOCK_NAME in receipt and INGREDIENT_MOCK_1["name"] in receipt and INGREDIENT_MOCK_2["name"] in receipt and str(expected_price) in receipt