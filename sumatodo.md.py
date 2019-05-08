def sumatodo(limite):
    resultado = 0
    for i in range(0, limite+1):
        resultado += i
    return resultado
print sumatodo(100)