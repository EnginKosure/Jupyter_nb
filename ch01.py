def combinations(*items):
    a = 1
    for i in items:
        if i != 0:
            a *= i
    return a
