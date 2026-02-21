import pytest
from unittest.mock import Mock

@pytest.fixture
def bun_mock():
    mock_bun = Mock()
    mock_bun.name = 'Каменная булка'
    mock_bun.price = 100
    mock_bun.get_price.return_value = 100
    mock_bun.get_name.return_value = 'Каменная булка'
    return mock_bun

@pytest.fixture
def ingredient_mock_1():
    mock_ingredient = Mock()
    mock_ingredient.name = 'Сыр'
    mock_ingredient.price = 50
    mock_ingredient.get_price.return_value = 50
    mock_ingredient.get_type.return_value = 'sauce'
    mock_ingredient.get_name.return_value = 'Сыр'
    return mock_ingredient

@pytest.fixture
def ingredient_mock_2():
    mock_ingredient = Mock()
    mock_ingredient.name = 'Колбаса'
    mock_ingredient.price = 75
    mock_ingredient.get_price.return_value = 75
    mock_ingredient.get_type.return_value = 'filling'
    mock_ingredient.get_name.return_value = 'Колбаса'
    return mock_ingredient