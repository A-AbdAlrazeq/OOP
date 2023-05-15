from Store import Store
from Products import Product

store1 = Store("Abood Store")
product1 = Product('Potatoes', 5.99, 'vegetable')
product2 = Product('Corn', 3.00, 'vegetable')
product3 = Product('Hamburger Meat', 8.15, 'meat')

store1.add_product(product1)
store1.add_product(product2)
store1.add_product(product3)
product1.update_price(2, True).print_info()
store1.inflation(2)
store1.set_clearance("vegetable", 2)
store1.products[0].print_info()
store1.products[1].print_info()
store1.products[2].print_info()

store1.sell_product(3)
store1.sell_product(2)
