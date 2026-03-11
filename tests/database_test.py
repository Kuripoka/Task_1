import pytest
from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from data import BUNS_DATA, INGREDIENTS_DATA

class TestDatabase:
    def test_available_buns_returns_correct_count(self):
        database = Database()
        assert len(database.available_buns()) == 3

    def test_available_ingredients_returns_correct_count(self):
        database = Database()
        assert len(database.available_ingredients()) == 6

    def test_database_has_sauces(self):
        database = Database()
        ingredients = database.available_ingredients()
        sauces = [ing for ing in ingredients if ing.get_type() == INGREDIENT_TYPE_SAUCE]
        assert len(sauces) == 3

    def test_database_has_fillings(self):
        database = Database()
        ingredients = database.available_ingredients()
        fillings = [ing for ing in ingredients if ing.get_type() == INGREDIENT_TYPE_FILLING]
        assert len(fillings) == 3

    @pytest.mark.parametrize("index,expected_name", [(i, data["name"]) for i, data in BUNS_DATA.items()])
    def test_database_bun_names(self, index, expected_name):
        database = Database()
        buns = database.available_buns()
        assert buns[index].get_name() == expected_name

    @pytest.mark.parametrize("index,expected_price", [(i, data["price"]) for i, data in BUNS_DATA.items()])
    def test_database_bun_prices(self, index, expected_price):
        database = Database()
        buns = database.available_buns()
        assert buns[index].get_price() == expected_price

    @pytest.mark.parametrize("index,expected_name", [(i, data["name"]) for i, data in INGREDIENTS_DATA.items()])
    def test_database_ingredient_names(self, index, expected_name):
        database = Database()
        ingredients = database.available_ingredients()
        assert ingredients[index].get_name() == expected_name

    @pytest.mark.parametrize("index,expected_price", [(i, data["price"]) for i, data in INGREDIENTS_DATA.items()])
    def test_database_ingredient_prices(self, index, expected_price):
        database = Database()
        ingredients = database.available_ingredients()
        assert ingredients[index].get_price() == expected_price
