numbers = {1: "one", 2:"two", 3: "tree", 4:"four"}
nums = [1, 2, 3, 4]

result = {num: num**2 for num in nums }

print( result)
# for key, value in numbers.items():
#     print(key,value)