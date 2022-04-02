from customer import Customer
from shopping_cart import ShoppingCart
from product import Product

product_one = Product('Potato', 2, 'Starch')
product_two = Product('Apple', 2, 'Fruit')
product_three = Product('Tomato', 4, 'Vegtable')
product_four = Product('Chicken', 10, "Meat")

customer_one = Customer('Steve')
print(customer_one.customer_name)
customer_one.customer_add_product(product_one)
customer_one.customer_add_product(product_four)
customer_one.customer_add_product(product_two)
customer_one.customer_show_product()
customer_one.shopping_cart.item_total()
customer_one.shopping_cart.empty_cart()
customer_one.shopping_cart.item_total()
