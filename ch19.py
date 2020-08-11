# def round_number(num, n):
#     floor_div = num//n
#     surplus = num % n
#     result = floor_div*n
#     if surplus >= n/2:
#         result += n

#     return result


# def round_number(num, n):
#     div, mod = divmod(num, n)
#     if mod >= n/2:
#         return div * n + n
#     return div * n


def round_number(num, n):
    mn = num//n*n
    mx = mn+n
    return mx if num-mn >= mx-num else mn


print(round_number(33, 25))  # ➞ 25

print(round_number(46, 7))  # ➞ 49

print(round_number(133, 14))  # ➞ 140
