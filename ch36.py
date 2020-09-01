# Given an array of integers, return a new array such that
# each element at index i of the new array is the product of
# all the numbers in the original array except the one at i.
# For example, if our input was [1, 2, 3, 4, 5],
# the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1],
# the expected output would be [2, 3, 6].
# Follow-up: what if you can't use division?


def find_product(l):
    prod = 1
    for i in l:
        prod *= i

    x = [int(prod/i) for i in l]
    print(x)


def myproducts(nums):
    return [int("".join(map(str, eval(str(i).replace(',', '*'))))) for i in [[nums[j] for j in range(len(nums)) if i != j] for i in range(len(nums))]]


find_product([1, 2, 3, 4, 5])
print(myproducts([3, 2, 1]))
