from collections import defaultdict

with open("data.csv", "r") as file:
    data=file.readlines()
data=[line.replace("\n", "") for line in data]
data=[line.split("\t") for line in data]
#s = sum([int(fila[1]) for fila in data])


d = defaultdict(int)

for linea in data:
    letras = linea[3].split(",")
    for l in letras:
        d[l] += int(linea[1])


print(dict(sorted(d.items())))


#punto 12
dic = defaultdict(int)

for fila in data:
    letra = fila[0]
    for l in fila[4].split(","):
        clave, valor = l.split(":")
        dic[letra] += int(valor)

print(dict(sorted(dic.items())))


