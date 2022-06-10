def fibbonaci(bounds):
    result = []
    a, b = 0, 1
    while a < bounds:
        result.append(a)
        a, b = b, a + b
    return result


print(fibbonaci(10000))