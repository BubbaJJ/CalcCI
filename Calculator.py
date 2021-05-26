class Calc:
    # Addition
    def add(x, y):
        return x + y

    # Subtraction
    def sub(x, y):
        return x - y

    # Multiplication
    def mul(x, y):
        return x * y

    # Division
    def div(x, y):
        return x / y

    # Squared / Power
    def power(x, y):
        return pow(x, y)

    # Modulus
    def modulo(x, y):
        return x % y

    # Checking number of letters in string
    # Returns true if counter is above 9
    def countChars(str):
        counter = sum(1 for i in str if i.isalpha())
        return bool(counter > 9)