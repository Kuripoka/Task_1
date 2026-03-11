import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:
    def test_ingredient_get_name(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "Острый соус", 100)
        name = ingredient.get_name()
        assert name == "Острый соус"
    def test_ingredient_get_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "Котлета", 150)
        price = ingredient.get_price()
        assert price == 150

    @pytest.mark.parametrize("ingredient_type", [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING])
    def test_ingredient_get_type(self, ingredient_type):
        ingredient = Ingredient(ingredient_type, "Ингредиент", 100)
        result_type = ingredient.get_type()
        assert result_type == ingredient_type

    def test_ingredient_constructor(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "Сметана", 200)
        assert (ingredient.type, ingredient.name, ingredient.price) == (INGREDIENT_TYPE_SAUCE, "Сметана", 200)