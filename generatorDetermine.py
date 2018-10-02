import math
import random as rnd
import matplotlib.pyplot as plt


def ravnomer(__a: float, __b: float, __R: float) -> float:
    assert 0 <= __R <= 1
    return __a + (__b - __a) * __R


def gauss(__mx: float, __sx: float, __RList: list) -> float:
    for __R in __RList:
        assert 0 <= __R <= 1
    n = len(__RList)
    return sum([x - n / float(2) for x in __RList]) * math.sqrt(12 / float(n)) * __sx + __mx


def exponential(__lambda: float, __R: float) -> float:
    assert 0 <= __R <= 1
    return (-1 / float(__lambda)) * math.log(__R)


def gamma(__lambda: float, __nu: float, __RList: list) -> float:
    for __R in __RList:
        assert 0 <= __R <= 1
    return (-1 / float(__lambda)) * sum([math.log(x) for x in __RList])


def triangleMax(__a: float, __b: float, __R1: float, __R2: float) -> float:
    assert 0 <= __R1 <= 1
    assert 0 <= __R2 <= 1
    return ravnomer(__a, __b, max(__R1, __R2))


def triangleMin(__a: float, __b: float, __R1: float, __R2: float) -> float:
    assert 0 <= __R1 <= 1
    assert 0 <= __R2 <= 1
    return ravnomer(__a, __b, min(__R1, __R2))


def simpson(__a: float, __b: float, __R1: float, __R2: float):
    assert 0 <= __R1 <= 1
    assert 0 <= __R2 <= 1
    return ravnomer(__a / float(2), __b / float(2), __R1) + ravnomer(__a / float(2), __b / float(2), __R2)


def getRandom():
    return rnd.uniform(0, 1)


def ravnomer_TEST() -> list:
    a = 1
    b = 51
    size = 1000000
    return [ravnomer(a, b, getRandom()) for _ in range(0, size)]


def gauss_TEST() -> list:
    mx = 25
    sx = 15
    n = 6
    size = 1000000
    return [gauss(mx, sx, [getRandom() for _ in range(0, n)]) for _ in range(0, size)]


def exponential_TEST() -> list:
    lam = 13
    size = 1000000
    return [exponential(lam, getRandom()) for _ in range(0, size)]


def gamma_TEST() -> list:
    lam = 13
    nu = 14
    n = 6
    size = 1000000
    return [gamma(lam, nu, [getRandom() for _ in range(0, n)]) for _ in range(0, size)]


def triangleMax_TEST() -> list:
    a = 1
    b = 51
    size = 1000000
    return [triangleMax(a, b, getRandom(), getRandom()) for _ in range(0, size)]


def triangleMin_TEST() -> list:
    a = 1
    b = 51
    size = 1000000
    return [triangleMin(a, b, getRandom(), getRandom()) for _ in range(0, size)]


def simpson_TEST() -> list:
    a = 1
    b = 51
    size = 1000000
    return [simpson(a, b, getRandom(), getRandom()) for _ in range(0, size)]


def showHist(__res: list, __output: str):
    offset = min(__res)
    step = (max(__res) - offset)/float(20)
    plt.hist(__res, bins=[i * step + offset for i in range(0, 21)])
    plt.savefig(__output)
    plt.show()

if __name__ == "__main__":
    showHist(ravnomer_TEST(), "ravnomer.png")
    showHist(gauss_TEST(), "gauss.png")
    showHist(exponential_TEST(), "exponential.png")
    showHist(gamma_TEST(), "gamma.png")
    showHist(triangleMax_TEST(), "triangleMax.png")
    showHist(triangleMin_TEST(), "triangleMin.png")
    showHist(simpson_TEST(), "simpson.png")