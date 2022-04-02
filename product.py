class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
    def description(self):
        return self.name,self.price,self.category

