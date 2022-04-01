class ShoppingCart:
    def __init__(self,):
        self.products = []

    def item_list(self):
        self.number_items = len(self.products)
        print(f'There are {self.number_items} items in this cart')
        print(self.products)
    def add_product(self):
        