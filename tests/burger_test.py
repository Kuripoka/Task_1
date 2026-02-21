import pytest
from praktikum.burger import Burger


class TestBurger:
    def test_burger_set_buns(self, bun_mock):
        burger = Burger()
        burger.set_buns(bun_mock)
        assert (burger.bun.name, burger.bun.price) == ('Каменная булка', 100)

    def test_burger_add_ingredient(self, ingredient_mock_1):
        burger = Burger()
        burger.add_ingredient(ingredient_mock_1)
        assert (burger.ingredients[0].name, burger.ingredients[0].price) == ('Сыр', 50)

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
        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_mock_1)
        burger.add_ingredient(ingredient_mock_2)
        assert burger.get_price() == 325

    def test_burger_get_receipt(self, bun_mock, ingredient_mock_1, ingredient_mock_2):
        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_mock_1)
        burger.add_ingredient(ingredient_mock_2)
        receipt = burger.get_receipt()
        assert 'Каменная булка' in receipt and 'Сыр' in receipt and 'Колбаса' in receipt and '325' in receipt