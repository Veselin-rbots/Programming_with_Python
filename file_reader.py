with open("numbers.txt", "r") as file:
    print([el[:-1] for el in file.readlines()])