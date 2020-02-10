# name: Adventure

import time


def cls():
    print('\n' * 50)


def start():
    cls()
    print('You are now using the Calculator')
    print('\n' * 4)
    print('note: when using calculator please use only numbers unless told otherwise.')
    ans = input('Type \'enter\' to start:\n').lower().strip()
    if ans == 'enter':
        calc()
    elif ans == 'back':
        print('- Returning -')
        time.sleep(0.5)
        from subprocess import call
        call(["python", "Startup.py"])
    elif ans == 'help':
        from subprocess import call
        call(["python", "Help.py"])
    else:
        print('Invalid input')
        time.sleep(0.5)
    while ans != '':
        start()


def calc():
    cls()

    # Program make a simple calculator
    # This function adds two numbers
    def add(x, y):
        return x + y

    # This function subtracts two numbers
    def subtract(x, y):
        return x - y

    # This function multiplies two numbers
    def multiply(x, y):
        return x * y

    # This function divides two numbers
    def divide(x, y):
        return x / y

    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    # Take input from the user
    choice = input("Enter (1/2/3/4):\n")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if choice == '1':
        print(num1, "+", num2, "=", add(num1, num2))
        time.sleep(1.5)
        calc()
    elif choice == '2':
        print(num1, "-", num2, "=", subtract(num1, num2))
        time.sleep(1.5)
        calc()
    elif choice == '3':
        print(num1, "*", num2, "=", multiply(num1, num2))
        time.sleep(1.5)
        calc()
    elif choice == '4':
        print(num1, "/", num2, "=", divide(num1, num2))
        time.sleep(1.5)
        calc()
    else:
        print("Invalid input")
        time.sleep(0.5)


cls()
start()
