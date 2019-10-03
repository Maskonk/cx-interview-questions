import json
import math


class ShoppingBasket:

    def __init__(self):
        self.basket = {}
        self.subtotal = 0
        self.discount = 0
        self.total = 0
        with open('shopping_basket/Catalogue.json', 'r') as f:
            self.catalogue = json.load(f)

        with open('shopping_basket/Offers.json', 'r') as f:
            self.offers = json.load(f)

    def add_item_to_basket(self, item):
        if item in self.catalogue.keys():
            if item in self.basket:
                self.basket[item] += 1
            else:
                self.basket[item] = 1
            self.subtotal += self.catalogue[item]
            self.discount = self.check_discount()
            self.total = round(self.subtotal - self.discount, 2)

    def remove_one_of_item_from_basket(self, item):
        if item in self.basket:
            self.basket[item] -= 1
            if self.basket[item] == 0:
                self.basket.pop(item)
            self.subtotal -= self.catalogue[item]

    def remove_all_of_item(self, item):
        if item in self.basket:
            self.subtotal -= self.basket[item] * self.catalogue[item]
            self.basket.pop(item)

    def check_discount(self):
        discount = 0
        for item in self.basket:
            if item in self.offers["get1free"]:
                if self.basket[item] >= self.offers["get1free"][item]["qualifying amount"]:
                    amount = math.floor(self.basket[item] / self.offers["get1free"][item]["qualifying amount"])
                    discount = amount * self.catalogue[item] * amount

        return discount
