from customer import Customer
from shopping_cart import ShoppingCart
from product import Product

customer_one = Customer('Steve')
print(customer_one.customer_name)
customer_one.customer_add_product()
customer_one.customer_add_product()
customer_one.customer_add_product()
customer_one.customer_show_product()
customer_one.shopping_cart.item_list()
customer_one.shopping_cart.empty_cart()
customer_one.shopping_cart.item_list()

