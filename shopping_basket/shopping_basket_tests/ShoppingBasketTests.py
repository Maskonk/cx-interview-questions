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