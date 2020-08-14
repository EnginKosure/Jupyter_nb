# https://edabit.com/challenge/6brSyFwWnb9Msu7kX


def pos_neg_sort(lst):
    a = sorted([x for x in lst if x > 0])
    for i in range(len(lst)):
        if lst[i] < 0:
            a.insert(i, lst[i])
    return a

# def pos_neg_sort(lst):
#   pos = sorted([i for i in lst if i>0],reverse=True)
#   return [pos.pop() if j>0 else j for j in lst]

# def pos_neg_sort(lst):
# 	positives = iter(sorted(i for i in lst if i > 0))
# 	return [next(positives) if i > 0 else i for i in lst]


print(pos_neg_sort([6, 3, -2, 5, -8, 2, -2]))  # ➞ [2, 3, -2, 5, -8, 6, -2]

print(pos_neg_sort([6, 5, 4, -1, 3, 2, -1, 1]))  # ➞ [1, 2, 3, -1, 4, 5, -1, 6]

print(pos_neg_sort([-5, -5, -5, -5, 7, -5]))  # ➞ [-5, -5, -5, -5, 7, -5]

print(pos_neg_sort([]))  # ➞ []
