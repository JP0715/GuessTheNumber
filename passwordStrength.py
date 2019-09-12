# passwordStrength.py. Determines password strength.
import re

while True:
    p = str(input('Enter a password: '))
    if len(p)<8:
        print('Weak password')
        break
    elif not re.search("[a-z]", p):
        print('Weak password')
        break
    elif not re.search("[A-Z]", p):
        print('Weak password')
        break
    elif not re.search("[0-9]", p):
        print('Weak password')
        break
    else:
        print('Strong password.')
        break
