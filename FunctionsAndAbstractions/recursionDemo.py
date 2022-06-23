def mult_iter(a, b):
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result

def mult(a, b):
    if b == 1:
        return a
    else:
        return a + mult(a, b -1)

def fact(n):
    if n == 1:
        return n
    else:
        return n * fact(n -1)

def gcdIter(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def gcdRecur(a, b):
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)

def fib(a):
    if a == 0 or a == 1:
        return 1
    else:
        return fib(a - 1) + fib(a - 2)

# print(mult_iter(2, 9))
# print(mult(2, 9))
# print(fact(4))
#print(12 % 9)
# print(gcdIter(9, 12))
# print(gcdRecur(9, 12))
print(fib(10))