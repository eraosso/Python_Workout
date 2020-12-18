import random


def guessing_game():
    number = random.randint(0, 100)
    name = input("What's your name? ")
    print(f'Hello, {name}!')
    guess = int(input(f'{name}, guess what number I have!'))

    while True:
        if guess > number:
            print(f' Your guess of {guess} is too high! Guess again:')
        if guess < number:
            print(f'Your guess of {guess} is too low! Guess again:')
        if guess == number:
            print(f'Just right! The number is {guess}!')
            break
        guess = int(input())
    return


guessing_game()
