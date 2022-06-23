def func_a():
    print("Function a")

def func_b(y):
    print("Inside function b")
    return y

def func_c(z):
    print("Inside function C")
    return z

print(func_a())
print(5 + func_b(2))
print(func_c(func_a()))