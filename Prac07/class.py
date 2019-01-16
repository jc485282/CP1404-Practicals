products = [["Phone", 340, False], ["PC", 1420.95, True], ["Plant", 24.5, True], ["Tree", 24.5, True]]

#on_sale_products = [product for product in products if product[2]]

#print(on_sale_products)

on_sale_products = max([product[1] for product in products])

maximum_price = 0
most_expensive_products = []
for product in products:
    if product[1] > maximum_price:
        maximum_price = product[1]
        most_expensive_products = [product]
    elif product[1] == maximum_price:
        most_expensive_products.append(product)


print(most_expensive_products)


class Product:
    def __init__(self, name="", price=0.0, on_sale=False):
        print("making a new item")
        self.name = name
        self.price = price
        self.is_on_sale = on_sale

    def put_on_sale(self):
        self.price *= 0.9
        self.is_on_sale = True

    def __str__(self):
        if self.is_on_sale:
            on_sale_str = "(on sale)"
        else:
            on_sale_str = ""
        return "{}, ${} {}".format(self.name, self.price, on_sale_str)

item = Product("iPhone X", 200, False)
item.put_on_sale()
print(item)

me = Product("Richa", 2.5, True)
print(me)