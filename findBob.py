s = 'azcbobobegghakl'
bobCount = 0
start = 0;

while start < len(s):
    currPos = s.find("bob", start)
    if currPos != -1:
        start = currPos + 1
        bobCount += 1
    else:
        break

# print(s.count("bob", 0, len(s)))

print('The number of times bob occurs is: ' + str(bobCount))