import pytest
from ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE
from burger import Burger, Bun, Ingredient
from unittest.mock import Mock


@pytest.fixture
def mock_bun():
    # Создает мок булочки с фиксированной ценой и названием
    bun = Mock(spec=Bun)
    bun.get_price.return_value = 5.0
    bun.get_name.return_value = "white bun"
    return bun

@pytest.fixture
def mock_ingredient_filling(ingredient_mock_factory):
    return ingredient_mock_factory(100, "cutlet", INGREDIENT_TYPE_FILLING)

@pytest.fixture
def mock_ingredient_sauce(ingredient_mock_factory):
    return ingredient_mock_factory(200, "hot sauce", INGREDIENT_TYPE_SAUCE)

@pytest.fixture
def burger_filled_with_ingredients(ingredient_mock_factory):
    burger = Burger()
    burger.add_ingredient(ingredient_mock_factory(100, "cutlet", INGREDIENT_TYPE_FILLING))
    burger.add_ingredient(ingredient_mock_factory(200, "potato", INGREDIENT_TYPE_FILLING))
    burger.add_ingredient(ingredient_mock_factory(300, "sausage", INGREDIENT_TYPE_FILLING))
    burger.add_ingredient(ingredient_mock_factory(400, "hot sauce", INGREDIENT_TYPE_SAUCE))
    burger.add_ingredient(ingredient_mock_factory(500, "sour cream", INGREDIENT_TYPE_SAUCE))
    burger.add_ingredient(ingredient_mock_factory(600, "chili sauce", INGREDIENT_TYPE_SAUCE))
    return burger


@pytest.fixture
def ingredient_mock_factory():
    def _create_ingredient_mock(price, name, type):
        ingredient = Mock(spec=Ingredient)
        ingredient.get_price.return_value = price
        ingredient.get_name.return_value = name
        ingredient.get_type.return_value = type
        return ingredient
    return _create_ingredient_mock


