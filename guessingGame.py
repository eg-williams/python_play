from random import randrange
guess = randrange(0,100,2)
numGuesses = 0
while(numGuesses != 5):
    currentGuess = int(input("Guess the number between 1 and 100:"))
    if currentGuess == guess:
        print("You are correct")
        print("The answer was %s" % guess)
        break
    else:
        remaining = 5 - numGuesses
        print("You have %s guesses remaining" % (remaining - 1))
        numGuesses += 1

print("The answer was %s" %guess)