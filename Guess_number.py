"""
Number guessing game
The number to guess will be from 1 to 20 (inclusive).
The user will have 3 guesses to guess the number correctly
After each wrong guess, the user will be told whether to guess higher or lower next time.
If the user doesn't win, tell them the number.
"""
import random

def run_game():
    System_number = random.randint(1,20)
    n = 0
    while n < 3:
        User_input = int(input("Guess a number"))
        if User_input == System_number:
            print('You\'re correct!')
            break
        elif User_input > System_number:
            print('It\'s smaller!')
            n+=1
        elif User_input < System_number:
            print('It\'s higher')
            n+=1
    print('The correct number was {}'.format(System_number))

run_game()