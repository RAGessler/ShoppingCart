from product import Product
from shopping_cart import ShoppingCart

class Customer:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.shopping_cart = ShoppingCart()
    def customer_add_product(self, item):
        self.shopping_cart.add_product(item)
    def customer_show_product(self):
        for item in range(len(self.shopping_cart.products)):
         shown_prodct = self.shopping_cart.products[item]
         print(shown_prodct.name)