# name: Help


import time


def cls():
    print('\n' * 50)


def hlp():
    cls()
    print('[list of commands]')
    print('help - list of commands')
    print('calc - opens Calculator')
    print('games - opens Games')
    print('back - returns to startup')
    print('exit - kills the program')
    ans = input('enter a command:\n').lower().strip()
    if ans == 'back':
        print('- Returning -')
        time.sleep(0.5)
        from subprocess import call
        call(["python", "Startup.py"])
    else:
        print('Invalid input')
        time.sleep(0.5)
    while ans != '':
        hlp()


hlp()
