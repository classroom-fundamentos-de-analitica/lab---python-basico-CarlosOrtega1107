with open("data.csv", "r") as file:
    data=file.readlines()
s = sum([int(fila[1]) for fila in data])