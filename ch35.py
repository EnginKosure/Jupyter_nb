# Write a function that takes a positive integer and calculates how many dots exist in a pentagonal shape around the center dot on the Nth iteration.


def pentagonal(n):
    if n == 1:
        return 1
    else:
        return 5*(n-1)+pentagonal(n-1)


print(pentagonal(1))  # ➞ 1

print(pentagonal(2))  # ➞ 6

print(pentagonal(3))  # ➞ 16

print(pentagonal(8))  # ➞ 141
