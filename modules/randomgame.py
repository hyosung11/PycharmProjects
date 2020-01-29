from random import randint
import sys
# generate a number between 1~10
answer = randint(int(sys.argv[1]), int(sys.argv[2]))

while True:
    try:
        # input from user?
        guess = int(input('Guess a number from 1 ~ 10 '))

        # check that input is a number 1~10
        if guess > 0 < 11:

            # check if number is the right guess. Otherwise ask again.
            if guess == answer:
                print('Wow, great guess. You\'re right!')
                break
        else:
            print('Out of range. Try again please')
    except ValueError:
        print('Please enter a number')
        continue



