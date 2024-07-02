from math import *
def giaiThua(N) :
    tich = 1
    for i in range(1, N + 1) :
        tich*= i

    return tich


def approx_sin(x, N) :
    sin_x = 0.0
    for i in range(N + 1) :
        sin_x+= ((-1) ** i) / giaiThua(2 * i + 1) * (x ** (2 * i + 1))

    return sin_x

def approx_cos(x, N) :
    cos_x = 0.0
    for i in range(N + 1) :
        cos_x+= ((-1) ** i) / giaiThua(2 * i) * (x ** (2 * i))

    return cos_x

def approx_sinh(x, N) :
    sinh_x = 0.0
    for i in range(N + 1) :
        sinh_x+= (x ** (2 * i + 1)) / giaiThua(2 * i + 1)

    return sinh_x

def approx_cosh(x, N) :
    cosh_x = 0.0
    for i in range(N + 1) :
        cosh_x+= (x ** (2 * i)) / giaiThua(2 * i)

    return cosh_x

