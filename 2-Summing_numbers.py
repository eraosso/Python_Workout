def mysum(*args):
    soma = 0
    for i in args:
        soma += i

    # return print("A soma total é: {}".format(soma))
    return soma

def mysum2(*args, start=0):
    soma = 0
    for i in args:
        soma += i

    # return print("A soma total é: {}".format(soma))
    return soma + start

def mysum3(lista = []):
    menor = len(lista[0])
    maior = len(lista[0])
    media = 0
    tamanhos = 0
    for palavra in lista:
        tamanhos += len(palavra)
        if len(palavra) <= menor:
            menor = len(palavra)
        elif len(palavra) >= maior:
            maior = len(palavra)

    return menor, maior, tamanhos/len(lista)

