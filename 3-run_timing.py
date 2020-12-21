def run_timing():
    tempo = 0
    tempos = []

    while tempo != "":
        tempo = input("Enter 10 Km run time: ")
        if tempo != "":
            tempos.append(float(tempo))

    s = sum(tempos)
    l = len(tempos)
    print("Average {}, over {} runs".format(s / l, l))


run_timing()


def float_inteiros(f, x, y):
    n = str(int(f))
    d = str(f - int(f))
    inteiro = float(n[-x:])
    decimal = d[2:2+y]
    return (inteiro + int(decimal) / (10 ** len(decimal)))

from decimal import *

def decimal_correto():
    decimal1 = Decimal(input('Entre um número decimal:'))
    decimal2 = Decimal(input('Entre um número decimal:'))

    print("A soma é {}".format(float(decimal1 + decimal2)))






