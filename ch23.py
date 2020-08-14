def pos_neg_sort(lst):
    a = sorted([x for x in lst if x > 0])
    for i in range(len(lst)):
        if lst[i] < 0:
            a.insert(i, lst[i])
    return a


print(pos_neg_sort([6, 3, -2, 5, -8, 2, -2]))  # ➞ [2, 3, -2, 5, -8, 6, -2]

print(pos_neg_sort([6, 5, 4, -1, 3, 2, -1, 1]))  # ➞ [1, 2, 3, -1, 4, 5, -1, 6]

print(pos_neg_sort([-5, -5, -5, -5, 7, -5]))  # ➞ [-5, -5, -5, -5, 7, -5]

print(pos_neg_sort([]))  # ➞ []
