"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    with open("data.csv", "r") as file:
        data=file.readlines()
    data=[line.replace("\n", "") for line in data]
    data=[line.split("\t") for line in data]
    return sum([int(fila[1]) for fila in data])


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    with open("data.csv", "r") as file:
        data=file.readlines()
    data=[line.replace("\n", "") for line in data]
    data=[line.split("\t") for line in data]
    #s = sum([int(fila[1]) for fila in data])


    d = {
        "A" : 0,
        "B": 0,
        "C": 0,
        "D": 0,
        "E": 0,
        }
    for fila in data:
        letra = fila[0]
        if letra in d:
            d[letra] += 1

    return list(d.items())



def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    with open("data.csv", "r") as file:
        data=file.readlines()
    data=[line.replace("\n", "") for line in data]
    data=[line.split("\t") for line in data]
    #s = sum([int(fila[1]) for fila in data])


    d = {
        "A" : 0,
        "B": 0,
        "C": 0,
        "D": 0,
        "E": 0,
        }
    for fila in data:
        letra = fila[0]
        if letra in d:
            d[letra] += int(fila[1])
    return list(d.items())


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    with open("data.csv", "r") as file:
        data=file.readlines()
    data=[line.replace("\n", "") for line in data]
    data=[line.split("\t") for line in data]
    #s = sum([int(fila[1]) for fila in data])


    d = {
        "01" : 0,
        "02": 0,
        "03": 0,
        "04": 0,
        "05": 0,
        "06": 0,
        "07": 0,
        "08": 0,
        "09": 0,
        "10": 0,
        "11": 0,
        "12": 0
        }

    fechas=[z[2].split("-") for z in data[0:]]
    for fecha in fechas:
        mes = fecha[1]
        if mes in d:
            d[mes] += 1
    return list(d.items())


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    with open("data.csv", "r") as file:
        data=file.readlines()
    data=[line.replace("\n", "") for line in data]
    data=[line.split("\t") for line in data]
    #s = sum([int(fila[1]) for fila in data])


    d = {
    "A" : [],
    "B": [],
    "C": [],
    "D": [],
    "E": [],
    }
    for fila in data:
        letra = fila[0]
        if letra in d:
            d[letra].append(int(fila[1]))

    return [(i[0], max(i[1]), min(i[1])) for i in d.items()]


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    from collections import defaultdict

    with open("data.csv", "r") as file:
        data=file.readlines()
    data=[line.replace("\n", "") for line in data]
    data=[line.split("\t") for line in data]
    #s = sum([int(fila[1]) for fila in data])

    columna5 = [f[4] for f in data]

    d = defaultdict(list)

    for linea in columna5:
        for cadena in linea.split(","):
            clave, valor = cadena.split(":")
            d[clave].append(int(valor))

    x = sorted(d.items())
    return [(i[0], min(i[1]), max(i[1])) for i in x]


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]
    """
    from collections import defaultdict

    with open("data.csv", "r") as file:
        data=file.readlines()
    data=[line.replace("\n", "") for line in data]
    data=[line.split("\t") for line in data]
    #s = sum([int(fila[1]) for fila in data])

    d = defaultdict(list)

    for fila in data:
        letra = fila[0]
        numero = int(fila[1])
        d[numero].append(letra)

    return sorted(d.items())


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    from collections import defaultdict

    with open("data.csv", "r") as file:
        data=file.readlines()
    data=[line.replace("\n", "") for line in data]
    data=[line.split("\t") for line in data]
    #s = sum([int(fila[1]) for fila in data])

    d = defaultdict(list)

    for fila in data:
        letra = fila[0]
        numero = int(fila[1])
        d[numero].append(letra)

    x = sorted(d.items())

    nuevo = []
    for tupla in x:
        nuevo.append((tupla[0], sorted(list(set(tupla[1])))))
    return nuevo


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    from collections import defaultdict

    with open("data.csv", "r") as file:
        data=file.readlines()
    data=[line.replace("\n", "") for line in data]
    data=[line.split("\t") for line in data]
    #s = sum([int(fila[1]) for fila in data])

    columna5 = [f[4] for f in data]

    d = defaultdict(int)

    for linea in columna5:
        for cadena in linea.split(","):
            clave, valor = cadena.split(":")
            d[clave] += 1

    return dict(sorted(d.items()))


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    with open("data.csv", "r") as file:
        data=file.readlines()
    data=[line.replace("\n", "") for line in data]
    data=[line.split("\t") for line in data]
    #s = sum([int(fila[1]) for fila in data])

    r = []
    for linea in data:
        letra = linea[0]
        n1 = len(linea[3].split(","))
        n2 = len(linea[4].split(","))

        r.append((letra, n1, n2))
    return r


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
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

    return dict(sorted(d.items()))


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    from collections import defaultdict
    with open("data.csv", "r") as file:
        data=file.readlines()
    data=[line.replace("\n", "") for line in data]
    data=[line.split("\t") for line in data]
    
    dic = defaultdict(int)

    for fila in data:
        letra = fila[0]
        for l in fila[4].split(","):
            clave, valor = l.split(":")
            dic[letra] += int(valor)

    return dict(sorted(dic.items()))
