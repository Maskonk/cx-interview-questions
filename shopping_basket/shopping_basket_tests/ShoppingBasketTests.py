from unittest import TestCase
from ..ShoppingBasket import ShoppingBasket


class TestShoppingBasket(TestCase):

    def setUp(self):
        self.shopping_basket = ShoppingBasket()

    def test_add_item_to_basket_one_item(self):
        self.shopping_basket.add_item_to_basket("Baked Beans")
        self.assertEqual({"Baked Beans": 1}, self.shopping_basket.basket)

    def test_add_item_to_basket_two_duplicate_items(self):
        self.shopping_basket.add_item_to_basket("Biscuits")
        self.shopping_basket.add_item_to_basket("Biscuits")
        self.assertEqual({"Biscuits": 2}, self.shopping_basket.basket)

    def test_add_item_to_basket_two_different_items(self):
        self.shopping_basket.add_item_to_basket("Biscuits")
        self.shopping_basket.add_item_to_basket("Baked Beans")
        self.assertEqual({"Baked Beans": 1, "Biscuits": 1}, self.shopping_basket.basket)

    def test_cannot_add_invalid_item_to_basket(self):
        self.shopping_basket.add_item_to_basket("Chocolate")
        self.assertEqual({}, self.shopping_basket.basket)

    def test_remove_one_item_from_basket(self):
        self.shopping_basket.add_item_to_basket("Baked Beans")
        self.shopping_basket.add_item_to_basket("Biscuits")
        self.shopping_basket.remove_one_of_item_from_basket("Baked Beans")
        self.assertEqual({"Biscuits": 1}, self.shopping_basket.basket)