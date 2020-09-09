# This is an interview question asked by Amazon.
# There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time.
# Given N, write a function that returns the number of unique ways you can climb the staircase.
#  The order of the steps matters.
# For example, if N is 4, then there are 5 unique ways:
# 1, 1, 1, 1
# 2, 1, 1
# 1, 2, 1
# 1, 1, 2
# 2, 2


# def unique_way(n):
#     import itertools
#     new_list = []
#     second_list = []
#     third_list = []
#     fourth_list = third_list
#     for i in range(0, n+1):
#         for j in range(0, n+1, 2):
#             if i + j == n:
#                 new_list.append([i, j])
#     for i in new_list:
#         second_list.append([i[0]*"1", int(i[1]/2)*"2"])
#     for i in second_list:
#         i[0] = int("".join(i[0]+i[1]))
#         third_list.append(i[0])
#     counter = -1
#     for i in third_list:
#         counter += 1
#         fourth_list[counter] = []
#         for j in str(i):
#             fourth_list[counter].append(int(j))
#     total_count = 0
#     for i in fourth_list:
#         total_count += len(set(itertools.permutations(i)))
#         print(*set(itertools.permutations(i)))
#     print(
#         f"For climb {n} steps staircase, there are {total_count} unique ways.")


# def steps(n):
#     if n <= 3:
#         return n
#     else:
#         return(steps(n-1) + steps(n-2))


def steps(n):
    return n if n <= 3 else (steps(n-1) + steps(n-2))


# steps(6)
# unique_way(10)
# unique_way(9)
print(steps(4))
