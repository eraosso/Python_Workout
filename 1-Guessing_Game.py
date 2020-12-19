import random


def guessing_game():
    number = random.randint(0, 100)
    name = input("What's your name? ")
    print(f'Hello, {name}!')
    guess = int(input(f'{name}, guess what number I have!'))

    cont = 0

    while cont < 5:
        if guess > number:
            print(f' Your guess of {guess} is too high! Guess again:')
            cont += 1
        if guess < number:
            print(f'Your guess of {guess} is too low! Guess again:')
            cont += 1
        if guess == number:
            print(f'Just right! The number is {guess}!')
            break
        guess = int(input())

    print(f' Sorry {name}. You have exceeded the number of guesses!')
    return


guessing_game()
