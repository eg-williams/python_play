an_letters = "aefhilmnorsxAEFHILMNORSX"
word = input("I'm gonna be your hypeman! Give me a word:")
times = int(input("Enthusiasm level (1-10):"))

i = 0

while i < len(word):
    char = word[i]
    if char in an_letters:
        print("Give me an " + char + "! " + char)
    else:
        print("Give me a " + char + "! " + char)
    i += 1
print("What do you have?")
for i in range(times):
    print(word, "!!!")
