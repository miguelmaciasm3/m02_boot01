from functools import reduce
lista = [1, 3, -1, 15, 9, 8]
sumatorio = reduce(lambda x, y: x + y, lista)
doble = map(lambda x: x*2, lista)
filtrar = filter(lambda x: x%2 == 0, lista)