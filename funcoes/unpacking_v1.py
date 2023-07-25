def soma_3(a, b, c):
    print(type(a))
    soma = a + b + c
    return soma 

numeros_tupla = (0, 2, 3)
print(soma_3(*numeros_tupla))

numeros_lista = [0, 1, 5]
print(soma_3(*numeros_lista))

