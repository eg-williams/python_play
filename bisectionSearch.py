
def find_square(guess):
    epsilon = 0.01
    guessCount = 0
    low = 0.0
    high = guess
    ans = (high + low) / 2.0
    while abs(ans ** 2 - guess) >= epsilon:
        #print('low = ' + str(low) + ' high = ' + str(high) + ' ans = ' + str(ans))
        guessCount += 1
        # Do we check the lower side or the upper side here?
        if ans**2 < guess:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2.0 # Now find a new mid-point
    print('Num guesses: ' + str(guessCount))
    print(str(ans) + ' is close to the square root of ' + str(guess))


def find_cube(cube):
    epsilon = 0.01
    guessCount = 0
    low = 0.0
    high = cube
    guess = (high + low) / 2.0

    while abs(guess ** 3 - cube) >= epsilon:
        if guess**3 < cube:
            low = guess
        else:
            high = guess
        guess = (high + low)/2.0
        guessCount += 1
    print('Num guesses: ' + str(guessCount))
    print(str(guess) + ' is close to the cube root of ' + str(cube))

find_square(25)

find_cube(5.2)