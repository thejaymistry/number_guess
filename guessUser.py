import random

def Computer_guess(x):
    low=1
    high=x
    feedback=''

    while feedback != 'c':
        if(low!=high):
          guess= random.randint(low,high)
        else:
            guess=low
        feedback =input(f'is {guess} too high (H),too low (L), or correct (c) ??')
        if feedback=='h' or feedback =='H':
            high=guess-1
        elif feedback=='l' or feedback =='L':
            low=guess+1

    print(f'Hurray ! you guessed it right ..the number is {guess}');

Computer_guess(10)
