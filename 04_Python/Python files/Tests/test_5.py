from opcode import hasname
import random
number = random.randint(1,100)

player = str(input('Enter your name: '))
print('Hello', player, ', Welcome in this Number Guessing Game, please select a number between 1 and 100')

tries = 0

while g_number!= number and tries<3:
    print( 'You have ' + str(3-tries) + ' tries left, try again')
    g_number = int(input('Enter a number:'))
    tries+=1

    g_number = int(input('Enter a number: '))

    if g_number > number:
        print('Your guess is too high!')
    elif g_number == number:
        print('Congratulations, you guessed the correct number!')
    else:
        print('Your guess is too low')

if g_number == number:
    print('You are the best!')
    print('You won in ' + str(tries) + 'attempts')
else:
    print('You lost the game, the correct number is ' + str(number))

