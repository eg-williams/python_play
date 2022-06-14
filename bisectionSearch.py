x = 25
epsilon = 0.01
guessCount = 0
low = 0.0
high = x
ans = (high + low) / 2.0

while abs(ans**2 - x) >= epsilon:
    print('low = ' + str(low) + ' high = ' + str(high) + ' ans = ' + str(ans))
    guessCount += 1
    # Do we check the lower side or the upper side here?
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low) / 2.0 # Now find a new mid-point
print('Num guesses: ' + str(guessCount))
print(str(ans) + ' is close to the square root of ' + str(x))