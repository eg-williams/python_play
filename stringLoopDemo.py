s = "abcdefghijklmnopqrstuvwxyz"

for index in range(len(s)):
    if s[index] == 'i' or s[index] == 'u':
        print("There is an i or u")

# s is an iterable in this context.
for char in s:
    if char == 'i' or char == 'u':
        print("There is an i or u")