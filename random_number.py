import random

anwser = random.randint(1,10)

guess = int(input("I'm thinking of a number between 1 and 10: "))

if anwser == guess:
    print('You are corect')
else:
    if anwser < guess:
        print('Nope, it\'s smaller')
    else:
        print('Nope, it\'s higher')

print('The number was {}'.format(anwser))