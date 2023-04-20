import random

User1 = input("What is your name?")
User2 = input("What is your name?")

card_names = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14'] 
# Name: shuffled deck
# Purpose: return a shufffled deck to user
# Input: None
# Output: list representing a shuffled deck
def shuffled_deck():
    basic_deck = list(range(2, 15)) * 4
    random.shuffle(basic_deck)
    print(basic_deck)
    return basic_deck


    def card_names(cards):
        if i == 2:
            return "2"
        if i == 3:
            return "3"
        if i == 4:
            return "4"
        if i == 5:
            return "5"
        if i == 6:
            return "6"
        if i == 7: 
            return "7"
        if i == 8:
            return "8"
        if i == 9: 
            return "9"
        if i == 10:
            return "10"
        if i == 11: 
            return '11'
        if i == 12:
            return '12'
        if i == 13:
            return '13'
        if i == 14:
            return '14'

shuffled_deck()

def player_turn(cards):
    # print('number of cards in list before pop' + str(lens(cards)))
    randcard = random,random.randrange(len(cards))
    cardval = cards.pop(randcard)
    # print('number of cards in list after pop' + str(len(cards)))
    # print(cardval)
    print('player drew card:' + str(cardval))

player_turn(shuffled_deck())

def gameloop():
    print(shuffled_deck())

gameloop(player_turn(shuffled_deck()))




 