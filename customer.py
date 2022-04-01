from shopping_cart import ShoppingCart

class Customer:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.shopping_cart = ShoppingCart()
    def customer_add_product(self):
        self.shopping_cart.add_product()
    def customer_show_product(self):
        for item in self.shopping_cart.products:
            print(item)