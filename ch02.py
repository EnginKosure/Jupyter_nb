# Write a function that returns True if two lists, when combined, form a consecutive sequence.
# consecutive_combo([7, 4, 5, 1], [2, 3, 6]) ➞ True

# consecutive_combo([1, 4, 6, 5], [2, 7, 8, 9]) ➞ False

# consecutive_combo([1, 4, 5, 6], [2, 3, 7, 8, 10]) ➞ False

# consecutive_combo([44, 46], [45]) ➞ True


def consecutive_combo(lst1, lst2):
    n_l = sorted(lst1+lst2)
    print(n_l)
    return all([True if len(n_l) == n_l[-1]-n_l[0]+1 else False for i in n_l])


print(consecutive_combo([7, 4, 5, 1], [2, 3, 6]))
print(consecutive_combo([1, 4, 5, 6], [2, 3, 7, 8, 10]))
print(consecutive_combo([1, 4, 5, 6], [2, 3, 7, 8, 10]))
