def normal(x):
    return x

def cuadrado(y):
    return y**2


def sumatodo(limite, f):
    resultado = 0
    for i in range(0, limite+1):
        resultado += f(i)
    return resultado

if __name__ == '__main__':
    print(sumatodo(100, normal))
    print(sumatodo(3, cuadrado))
