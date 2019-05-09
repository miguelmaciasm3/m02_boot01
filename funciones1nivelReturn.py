def maximo(*l):
    if len(l) == 0:
        return 0
    m = l[0]
    for ix in range(1, len(l)):
        if l[ix] > m:
            m = l[ix]
    return m
def minimo(*l):
    if len(l) == 0:
        return 0
    m = l[0]
    for ix in range(1, len(l)):
        if l[ix] < m:
            m = l[ix]
    return m
def media(*l):
    if len(l) == 0:
        return 0
    acumulador = 0
    for ix in range(0, len(l)):
        acumulador += l[ix]
    
    return acumulador / len(l)
def returnf(nombre):
    nombre = nombre.lower()
    if nombre in funciones.keys():
        return (funciones[nombre])
    
    return None

funciones = {
    'max': maximo,
    'min': minimo,
    'med': media
    }
print(returnf('max')(1, 3, -1, 15, 9))
print(returnf('min')(1, 3, -1, 15, 9))
print(returnf('med')(1, 3, -1, 15, 9))
