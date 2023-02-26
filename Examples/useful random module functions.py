import random

print(random.randint(1, 6))    # Random int between 1 and 6. PSEUDORANDOM
print(random.random())         # Random float between 0 and 1. PSEUDORANDOM

myList = ['rock', 'paper', 'scissors']
print(random.choice(myList))    # Random choice from myList

cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]

random.shuffle(cards)

print(cards)
