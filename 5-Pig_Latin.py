def pig_latin(string):
    if string[0] in 'aeiou':
        return f'{string}way'
    else:
        return f'{string[1:]}{string[0]}ay'

print(pig_latin('eatpython'))


def pig_latin2(string):
    if string == string.capitalize():
        if string[0] in 'AEIOU':
            return f'{string}way'
        else:
            return f'{string[1:]}{string[0]}ay'
    else:
        if string[0] in 'aeiou':
            return f'{string}way'
        else:
            return f'{string[1:]}{string[0]}ay'

print(pig_latin2('Eatython'))

import string

def pig_latin3(word):
    acento=''

    if word[-1] in string.punctuation:
        acento = word[-1]
        word = word[0:-1]
    if word == word.capitalize():
        if word[0] in 'AEIOU':
            return f'{word}way{acento}'
        else:
            return f'{word[1:]}{word[0]}ay{acento}'
    else:
        if word[0] in 'aeiou':
            return f'{word}way{acento}'
        else:
            return f'{word[1:]}{word[0]}ay{acento}'

print(pig_latin3('python?'))

def pig_latin4(word):
    conta = 0
    for letra in word:
        if letra in 'aeiou':
            conta += 1
    if conta == 2:
        return f'{word}way'
    else:
        return f'{word[1:]}{word[0]}ay'

print(pig_latin4('wind'))

