from __future__ import print_function
import random


def food_id(food):
    fruits = ['apple', 'banana', 'orange']
    citrus = ['orange']
    starchy = ['banana', 'potato']

    if food in fruits:
        if food in citrus:
            return 'Citrus, Fruit'
        else:
            return 'NOT Citrus, Fruit'
    else:
        if food in starchy:
            return 'Starchy, NOT Fruit'
        else:
            return 'NOT Starchy, NOT Fruit'


print(food_id('apple'))
print(food_id('potato'))
print(food_id('orange'))
print(food_id('shit'))


def food_id_test():
    works = True
    if food_id('orange') != 'Citrus, Fruit':
        works = 'orange bug in food id()'
    if food_id('apple') != 'NOT Citrus, Fruit':
        works = 'apple bug in food_id()'
    if food_id('potato') != 'Starchy, NOT Fruit':
        works = 'potato bug'
    if food_id('other') != 'NOT Starchy, NOT Fruit':
        works = 'stupid'

    if works:
        print("All good!")
        return True
    else:
        print(works)
        return False


food_id('orange')
food_id_test()


def guess_once():
    secret = random.randint(1, 4)
    print('I have a number between 1 and 4.')
    guess = int(input('Guess: '))
    if guess > secret:
        print('Too big. Number was ', secret, '.', sep='')
    elif guess < secret:
        print('Too small. Number was ', secret, '.', sep='')
    else:
        print('Good job. The number was', guess, end='!\n')


guess_once()


def f(x):
    if int(x) == x:
        if x % 2 == 0:
            if x % 3 == 0:
                print(str(x) + " is a multiple of 6.")
            else:
                print(str(x) + " is even.")
        else:
            print(str(x) + " is odd.")
    else:
        print(str(x) + " is not an integer.")


f(100)
f(3)
f(12)
f(2.2)


def quiz_decimal(low, high):
    win = False
    while win == False:
        guess = float(input("Type a number between " + str(low) + " and " + str(high) + ": "))
        if guess > low and guess < high:
            print("Good!", str(low), "<", str(guess), "<", str(high))
            win = True
        elif guess < low:
            print("No,", str(guess), "is less than", str(low))
        else:
            print("No,", str(guess), "is greater than", str(high))


quiz_decimal(10, 10.5)