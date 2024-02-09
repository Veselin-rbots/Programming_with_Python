products = {}
product_data = input()

while not product_data == "statistics":
    product, quantity = product_data.split(": ")
    quantity = int(quantity)
    if product in products:
        products[product] += quantity
    else:
        products[product] = quantity
    product_data = input()

print(products)
