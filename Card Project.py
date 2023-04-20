import random

Card_values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'K', 'Q']
suits = ['Spades', 'Clubs', 'Diamonds', 'Hearts']

def pick5cards():
    
    Count = 0
    while Count < 5:
        randomValue = Card_values[random.randint(0, 12)]
        randomSuit = suits[random.randint(0, 3)]
        print("You've Drawn a" + randomValue + 'of' + randomSuit)
        Count += 1

pick5cards()
