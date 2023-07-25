def soma_n (*numeros):
    print(type(numeros))
    soma = 0
    for n in numeros:
        soma += n
    return soma

print(soma_n(2,4,4))