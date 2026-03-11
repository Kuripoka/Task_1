import pytest
from unittest.mock import Mock
from data import BUN_MOCK_NAME, BUN_MOCK_PRICE, INGREDIENT_MOCK_1, INGREDIENT_MOCK_2

@pytest.fixture
def bun_mock():
    mock_bun = Mock()
    mock_bun.name = BUN_MOCK_NAME
    mock_bun.price = BUN_MOCK_PRICE
    mock_bun.get_price.return_value = BUN_MOCK_PRICE
    mock_bun.get_name.return_value = BUN_MOCK_NAME
    return mock_bun

@pytest.fixture
def ingredient_mock_1():
    mock_ingredient = Mock()
    mock_ingredient.name = INGREDIENT_MOCK_1["name"]
    mock_ingredient.price = INGREDIENT_MOCK_1["price"]
    mock_ingredient.get_price.return_value = INGREDIENT_MOCK_1["price"]
    mock_ingredient.get_type.return_value = INGREDIENT_MOCK_1["type"]
    mock_ingredient.get_name.return_value = INGREDIENT_MOCK_1["name"]
    return mock_ingredient

@pytest.fixture
def ingredient_mock_2():
    mock_ingredient = Mock()
    mock_ingredient.name = INGREDIENT_MOCK_2["name"]
    mock_ingredient.price = INGREDIENT_MOCK_2["price"]
    mock_ingredient.get_price.return_value = INGREDIENT_MOCK_2["price"]
    mock_ingredient.get_type.return_value = INGREDIENT_MOCK_2["type"]
    mock_ingredient.get_name.return_value = INGREDIENT_MOCK_2["name"]
    return mock_ingredient