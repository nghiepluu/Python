"Randomly returns a number from 1 to 6"

import random


number1 = random.randint(1, 6)
number2 = random.randint(1, 6)
print("You rolled a " + str(number1) + " and a " + str(number2))

def add(n1, n2):
    print("I got 2 numner")
    print(n1)
    print(n2)
    result = n1 + n2
    print(result)
    return n1 + n2

print(add(1,2))
print(add(-1231, 123123))