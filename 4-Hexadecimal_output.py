def hex_output():
    numero = input('Enter an integer number:')
    numero_dec = 0
    for power, factor in enumerate(reversed(numero)):
        numero_dec += int(factor, 16) * (16 ** power)

    print('Hex {} is decimal {}'.format(numero, numero_dec))

hex_output()

def hex_output_2():
    numero = input('Enter an integer number:')
    numero_dec = 0
    for power, factor in enumerate(reversed(numero)):
        numero_dec += ord(chr(factor)) * (16 ** power)

    print('Hex {} is decimal {}'.format(numero, numero_dec))

def triangle_name():
    nome = input('Informe seu nome: ')
    for indice, letra in enumerate(nome):
        # print(letra * (indice + 1))
        print(nome[:indice + 1])
