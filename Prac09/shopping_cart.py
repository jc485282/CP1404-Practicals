"""
Do this now - start with the cart class
create a shopping program that uses that classes Product and Cart
A Cart can store multiple products in it
 - find out the current total price
 - add and remove products
 - display all products sorted by price


 """
 


class Cart:
    def __init__(self):
        self.products = []

    def __str__(self):
        return str([str(product) for product in self.products])

    def add(self, product):
        self.products.append(product)

    def remove(self, product):
        self.products.remove(self, product)

    def get_number_of_products(self):
        return len(self.products)


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price




