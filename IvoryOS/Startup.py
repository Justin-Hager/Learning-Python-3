# name: Startup
# date: 2020-01-21
# creator: Justin Hager

import time


def cls():
    print('\n' * 50)


def loading():
    cls()
    print('-Loading-')
    time.sleep(1)
    cls()


def startup():
    ivos = '- IvoryOS -'
    print(ivos)
    print('\n' * 5)
    commands()


def commands():
    print('Type \'help\' for list of commands')
    ans = input('Enter a command:\n').lower().strip()
    if ans == 'help':
        from subprocess import call
        call(["python", "Help.py"])
    elif ans == 'end':
        exit()
    elif ans == 'games':
        games()
    elif ans == 'calc':
        from subprocess import call
        call(["python", "Calculator.py"])
    else:
        print('Invalid input')
        time.sleep(0.5)
        cls()
    while ans != '':
        startup()


def games():
    cls()
    print('c:/users/ivory/games')
    print('- Adventure -')
    print('#\n' * 4)
    ans = input('Enter a command:\n').lower().strip()
    if ans == 'back':
        startup()
    if ans == 'adventure':
        from subprocess import call
        call(["python", "Adventure.py"])
    else:
        print('Invalid input')
        time.sleep(0.5)
    while ans != '':
        cls()
        games()


def calc():
    print('c/users/ivory/applications')
    input('[calculator]')
    from subprocess import call
    call(["python", "Calculator.py"])


loading()
startup()
