class ShoppingCart:
    def __init__(self):
        self.products = []
    def item_list(self):
        self.number_items = len(self.products)
        print(f'There are {self.number_items} items in this cart')
        print(self.products)
    def add_product(self):
        self.products.append(input('Throw someting into the cart.')) 
    def empty_cart(self):
        self.products.clear()

# my_cart = ShoppingCart()


# my_cart.add_product()
# my_cart.item_list()
# my_cart.empty_cart()
# my_cart.item_list()