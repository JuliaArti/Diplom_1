from ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE

test_add_ingredient_cases = [ 
    (INGREDIENT_TYPE_FILLING, "cutlet", 100),
    (INGREDIENT_TYPE_FILLING, "dinosaur", 200),
    (INGREDIENT_TYPE_FILLING, "sausage", 300),
    (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
    (INGREDIENT_TYPE_SAUCE, "sour cream", 200),
    (INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
]  

test_get_price_cases = [
        (5.0, [2.0, 3.0], 15.0),  # 2 булки + 2 ингредиента
        (3.0, [], 6.0),           # Только булки
        (4.0, [1.5], 9.5),        # Булки + 1 ингредиент
]        

test_get_receipt_cases = [
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
]