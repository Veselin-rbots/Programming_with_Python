number = float(input())

if number == 0:
    print("zero")
elif number > 0 and number < 1:
    print("small positive")
elif number >= 1 and number <= 1000000:
    print("positive")
elif 0 > number > -1:
    print("small negative")
elif 0 > number > -1:
    print("small negative")
elif number > 1000000:
    print("large positive")
elif -1 >= number >= -100000:
    print("negative")
else:
    print("large negative")