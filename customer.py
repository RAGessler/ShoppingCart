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

my_customer = Customer('john')
my_customer.customer_add_product()
my_customer.customer_show_product()