from random import randint
#Guess the number.

guessesTaken = 0

print("Enter a number from 1-10. You get 3 guesses. Enter 'x' to quit.")

number = str(randint(1, 11))

while guessesTaken < 4:
    guess = str(input("Enter a guess: "))
    guessesTaken += 1
    if guess == 'x':
        break
    if guess < number:
        print("Too low.")
    if guess > number:
        print("Too high.")
    if guess == number:
        break

if guess == number:
    print("Correct. The number was " + str(number) + '. You guessed the number in ' + 
    str(guessesTaken) + ' guesses.' )
    
if guess != number:
    print('The number was ' + str(number) + '.')






        




