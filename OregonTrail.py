import random
import datetime


def travel():
    miles_traveled = random.randint(38, 61)
    days_spent = random.randint(3, 8)

    print("You've traveled " + str(miles_traveled) + " miles it took " + str(days_spent) +" days")


def rest():
    health_increase = random.randrange(1,6)
    days_spent = random.randrange(2,6)
    
    print("You've gained +" + str(health_increase) + " health it took " + str(days_spent) + " days")
    

def hunt():
    animal = 100
    days_spent = random.randrange(2, 6)

    print("You've gained " + str(animal) + " lbs of food, and it took " + str(days_spent) + " days")


def help_function():
    commands = ['Travel', 'Rest', 'Hunt', 'Status', 'Help']
    print(commands)


date = ''
health = 5
food = 500
days_left = 336
travel_distance = 2000
while days_left > 0:


    travel()
rest()
hunt()
help_function()