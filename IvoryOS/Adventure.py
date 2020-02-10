# name: Adventure

import time


def cls():
    print('\n' * 50)


def game():
    cls()
    print('Welcome to TXT Adventure')
    print('\n' * 5)
    ans = input('Type \'play\' to start:\n')
    if ans == 'play':
        print('[WIP]')
        time.sleep(1)
        game()
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
        game()


cls()
game()
