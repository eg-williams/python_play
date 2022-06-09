#s = 'azcbobobegghakl'
# s = 'abcbcd'
s = 'iosolyzztnkdnidjhclf'
#

string_length = len(s)

longest_substr = s[0]
current_length_sub = s[0] # current length sub

for i in range(1, string_length):
    if s[i] >= s[i - 1]:
        current_length_sub += s[i]
    else:
        current_length_sub = s[i]
    if len(current_length_sub) > len(longest_substr):
        longest_substr = current_length_sub

print(longest_substr)

