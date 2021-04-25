from Calculator import Calc
from enum import Enum


class operators(Enum):
    Addition = 1
    Subtraction = 2
    Multiplication = 3
    Division = 4
    Modulus = 5
    Power = 6


def welcome():
    print("Welcome to the world of calculations! \n")
    # name = input("What's your name? ")
    # print("Okay, " + name + "! Are you ready for some calculations?!\n")


def calculations():
    print('''Today's options are:
    1. ''' + operators(1).name + '''
    2. ''' + operators(2).name + '''
    3. ''' + operators(3).name + '''
    4. ''' + operators(4).name + '''
    5. ''' + operators(5).name + '''
    6. ''' + operators(6).name)

    operator = operation()

    x = int(input("Pick your first number: "))
    y = int(input("Nice! Now pick your second number: "))

    if operator == 1:
        print('{} + {} = {}'.format(x, y, Calc.add(x, y)))

    elif operator == 2:
        print('{} - {} = {}'.format(x, y, Calc.sub(x, y)))

    elif operator == 3:
        print('{} * {} = {}'.format(x, y, Calc.mul(x, y)))

    elif operator == 4:
        if (y == 0):
            print("Nice try...")
        else:
            print('{} / {} = {}'.format(x, y, Calc.div(x, y)))

    elif operator == 5:
        print('{} % {} = {}'.format(x, y, Calc.modulo(x, y)))

    elif operator == 6:
        print('{} ** {} = {}'.format(x, y, Calc.power(x, y)))

    again()


def operation():
    choice = int(
        input("\nWhat would you like to do?(1-" + str(len(operators)) + "): "))
    if choice > 0 and choice < 7:
        print(operators(choice).name + " it is!\n")
        return choice
    else:
        print("Are you sure...?")
        operation()


def again():
    print("That concludes our magical adventure together!")
    answer = input("Wanna try again?! (Y/N) ")
    if answer.upper() == "Y":
        calculations()
    elif answer.upper() == "N":
        print("\nWell... I don't like you either.. so.. bye!\n")
    else:
        print("ok, let's try this again... \n")
        print("So what I said was: ", end="", flush=True)
        again()


welcome()
calculations()
