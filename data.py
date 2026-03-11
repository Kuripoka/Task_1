from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

BUN_MOCK_NAME = 'Каменная булка'
BUN_MOCK_PRICE = 100
INGREDIENT_MOCK_1 = {"name": "Сыр", "price": 50, "type": "sauce"}
INGREDIENT_MOCK_2 = {"name": "Колбаса", "price": 75, "type": "filling"}

BUNS_DATA = {
    0: {"name": "black bun", "price": 100},
    1: {"name": "white bun", "price": 200},
    2: {"name": "red bun", "price": 300},
}

INGREDIENTS_DATA = {
    0: {"name": "hot sauce", "price": 100, "type": INGREDIENT_TYPE_SAUCE},
    1: {"name": "sour cream", "price": 200, "type": INGREDIENT_TYPE_SAUCE},
    2: {"name": "chili sauce", "price": 300, "type": INGREDIENT_TYPE_SAUCE},
    3: {"name": "cutlet", "price": 100, "type": INGREDIENT_TYPE_FILLING},
    4: {"name": "dinosaur", "price": 200, "type": INGREDIENT_TYPE_FILLING},
    5: {"name": "sausage", "price": 300, "type": INGREDIENT_TYPE_FILLING},
}
