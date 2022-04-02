from product import Product
class ShoppingCart:
    def __init__(self):
        self.products = []
    def item_total(self):
        self.total_cost = 0
        for item in range(len(self.products)):
            self.total_cost += self.products[item].price
    def add_product(self, item):
        self.products.append(item) 
    def empty_cart(self):
        print('emptying cart...')
        self.products.clear()
