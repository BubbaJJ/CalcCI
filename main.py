from Calculator import Calc
from enum import Enum
from datetime import datetime


class operators(Enum):
    Addition = 1
    Subtraction = 2
    Multiplication = 3
    Division = 4
    Modulus = 5
    Power = 6


def output_to_txt(filename, data):
    with open(filename, 'a') as f:
        f.write(data)


def main():
    def welcome():
        print("Welcome to the world of calculations! \n")

    def calculations():
        ask_for_name()
        show_options()
        operator = set_operator()
        x, y = get_numbers()
        do_calculation(operator, x, y)
        ask_to_run_again()

    def ask_for_name():
        name = input("What's your name? ")
        print("Okay, " + name + "! Are you ready for some calculations?!\n")

    def get_numbers():
        x = int(input("Pick your first number: "))
        y = int(input("Now pick your second number: "))
        return x, y

    def set_operator():
        choice = int(
            input("\nWhich operator?(1-" + str(len(operators)) + "): "))
        if choice > 0 and choice < 7:
            print(operators(choice).name + " it is!\n")
            return choice
        else:
            print("Are you sure...?")
            set_operator()

    def do_calculation(operator, x, y):
        if operator == 1:
            result = Calc.add(x, y)
            print('{} + {} = {}'.format(x, y, result))

        elif operator == 2:
            result = Calc.sub(x, y)
            print('{} - {} = {}'.format(x, y, result))

        elif operator == 3:
            result = Calc.mul(x, y)
            print('{} * {} = {}'.format(x, y, result))

        elif operator == 4:
            if (y == 0):
                result = "Nice try..."
                print(result)
            else:
                result = Calc.div(x, y)
                print('{} / {} = {}'.format(x, y, result))

        elif operator == 5:
            result = Calc.modulo(x, y)
            print('{} % {} = {}'.format(x, y, result))

        elif operator == 6:
            result = Calc.power(x, y)
            print('{} ** {} = {}'.format(x, y, result))

        data = data_to_output(operator, x, y, result)
        output_to_txt('history.txt', data)

    def show_options():
        print('''Today's options are:
        1. ''' + operators(1).name + '''
        2. ''' + operators(2).name + '''
        3. ''' + operators(3).name + '''
        4. ''' + operators(4).name + '''
        5. ''' + operators(5).name + '''
        6. ''' + operators(6).name)

    def data_to_output(operator, x, y, result) -> str:
        new_Row = "\n"
        output_data = datetime.now().strftime("%Y-%m-%d %H:%M:%S") + new_Row
        output_data += "Chosen operator: " + operators(operator).name + new_Row
        output_data += "First number: " + str(x) + new_Row
        output_data += "Second number: " + str(y) + new_Row
        output_data += "Result: " + str(result) + new_Row
        output_data += new_Row

        return output_data

    def ask_to_run_again():
        print("That concludes our magical adventure together!")
        answer = input("Wanna try again?! (Y/N) ")
        if answer.upper() == "Y":
            calculations()
        elif answer.upper() == "N":
            print("\nWell... I don't like you either.. so.. bye!\n")
        else:
            print("ok, let's try this again... \n")
            print("So what I said was: ", end="", flush=True)
            ask_to_run_again()

    welcome()
    calculations()


if __name__ == '__main__':
    main()
