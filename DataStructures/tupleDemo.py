# te = (2,7,"bob")
#
# print(te + (8, 9, "tookokok"))
#
# print(te)
#
# print(te[1])
#
def quotient_and_remainder(x,y):
    q = x //y
    r = x % y
    return (q, r)



def get_data(aTuple):
    nums = ()
    words = ()
    for t in aTuple:
        nums = nums + (t[0],)
        if t[1] not in words:
            words = words + (t[1],)
    min_nums = min(nums)
    max_nums = max(nums)
    unique_words = len(words)
    return (min_nums, max_nums, unique_words)


(small, large, words) = get_data(((1, "mine"),(2, "yours")))