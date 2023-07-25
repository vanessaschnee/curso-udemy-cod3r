from math import pi


def circulo(raio):
    areaCirculo = pi * raio **2
    print(areaCirculo)


if __name__ == '__main__':
    raio = float(input("Digite o raio: "))
    circulo(raio)
        