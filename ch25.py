def split(n):
    return n if n < 5 else 3*split(n-3)


print(split(5))  # ➞ 6
# 3 times 2

print(split(10))  # ➞ 36
# 3 * 3 * 4

print(split(1))  # ➞ 1
