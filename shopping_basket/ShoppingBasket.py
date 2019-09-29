import json


class ShoppingBasket:

    def __init__(self):
        self.basket = {}
        with open('shopping_basket/Catalogue.json', 'r') as f:
            self.catalogue = json.load(f)

    def add_item_to_basket(self, item):
        if item in self.catalogue.keys():
            if item in self.basket:
                self.basket[item] += 1
            else:
                self.basket[item] = 1

