import pytest
from ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE
from burger import Burger

class TestBurger:
    # Тесты для класса Burger с использованием моков и параметризации

      
    def test_set_buns(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    @pytest.mark.parametrize("ingredient_type,name,price", [ 
           (INGREDIENT_TYPE_FILLING, "cutlet", 100),
           (INGREDIENT_TYPE_FILLING, "dinosaur", 200),
           (INGREDIENT_TYPE_FILLING, "sausage", 300),
           (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
           (INGREDIENT_TYPE_SAUCE, "sour cream", 200),
           (INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
    ])    
    def test_add_ingredient(self, ingredient_mock_factory, ingredient_type, name, price):
        burger = Burger()
        ingredient = ingredient_mock_factory(price, name, ingredient_type)
        burger.add_ingredient(ingredient)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient
    
    def test_add_multiple_ingredients(self, burger_filled_with_ingredients, mock_ingredient_filling):
        burger = burger_filled_with_ingredients
        burger.add_ingredient(mock_ingredient_filling)
        assert len(burger.ingredients) == 7
        assert burger.ingredients[6] == mock_ingredient_filling

    def test_remove_ingredient(self, mock_ingredient_filling):
        burger = Burger()
        burger.add_ingredient(mock_ingredient_filling)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient(self, burger_filled_with_ingredients, mock_ingredient_filling, mock_ingredient_sauce):
        burger = burger_filled_with_ingredients
        burger.add_ingredient(mock_ingredient_filling)
        burger.add_ingredient(mock_ingredient_sauce)
        
        burger.move_ingredient(6, 7)
        
        assert burger.ingredients[6] == mock_ingredient_sauce
        assert burger.ingredients[7] == mock_ingredient_filling

    @pytest.mark.parametrize("bun_price, ingr_prices, expected_price", [
        (5.0, [2.0, 3.0], 15.0),  # 2 булки + 2 ингредиента
        (3.0, [], 6.0),           # Только булки
        (4.0, [1.5], 9.5),        # Булки + 1 ингредиент
    ])
    def test_get_price(self, ingredient_mock_factory, mock_bun, bun_price, ingr_prices, expected_price):
        mock_bun.get_price.return_value = bun_price
        burger = Burger()
        burger.set_buns(mock_bun)
        
        for price in ingr_prices:
            ingr_mock = ingredient_mock_factory(price, "cheese", INGREDIENT_TYPE_FILLING)
            ingr_mock.get_price.return_value = price
            burger.add_ingredient(ingr_mock)
        
        assert burger.get_price() == expected_price

    @pytest.mark.parametrize("bun_name, bun_price, ingredients, expected_receipt", [
        (
            "white bun",
            3.0,
            [
                (INGREDIENT_TYPE_FILLING, "cheese", 4.0),
                (INGREDIENT_TYPE_SAUCE, "ketchup", 5.0)
            ],
            '(==== white bun ====)\n'
            '= filling cheese =\n'
            '= sauce ketchup =\n'
            '(==== white bun ====)\n\n'
            'Price: 15.0'
        ),
        (
            "dark bun",
            3.0,
            [],
            '(==== dark bun ====)\n'
            '(==== dark bun ====)\n\n'
            'Price: 6.0'
        )
    ])
    def test_get_receipt(self, ingredient_mock_factory, mock_bun, bun_name, bun_price, ingredients, expected_receipt):
        mock_bun.get_name.return_value = bun_name
        mock_bun.get_price.return_value = bun_price
        
        burger = Burger()
        burger.set_buns(mock_bun)
        
        for ingr_type, ingr_name, ingr_price in ingredients:
            ingr_mock = ingredient_mock_factory(ingr_price, ingr_name, ingr_type)
            burger.add_ingredient(ingr_mock)
        
        assert burger.get_receipt() == expected_receipt