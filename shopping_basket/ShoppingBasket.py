import json


class ShoppingBasket:

    def __init__(self):
        self.basket = {}
        with open('Catalogue.json', 'r') as f:
            self.catalogue = json.load(f)

    def add_item_to_basket(self, item):
        pass

