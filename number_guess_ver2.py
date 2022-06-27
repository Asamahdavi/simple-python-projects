import random

def guessFun(x):
    rand = random.randint(1,x)
    guess = 0 
    guesses=0;
    while guess != rand:
        guesses+=1
        guess =int(input(f'Please Guess a number between 1 and {x}: '))

        if guess < rand:
            print('Guess again. too low')
        elif guess>rand:
            print('Guess again. Too high')

    print("You got it in",guesses,"guesses")



guessFun(20)

