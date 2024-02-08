data = input().split()

products = {}

for index in range(0, len(data), 2):
    key = data[index]
    value = data[index + 1]
    products[key] = value
    # a = 5

print(products)
