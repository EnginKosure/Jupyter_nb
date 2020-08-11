def round_number(num, n):
    floor_div = num//n
    surplus = num % n
    result = floor_div*n
    if surplus >= n/2:
        result += n

    return result


print(round_number(33, 25))  # ➞ 25

print(round_number(46, 7))  # ➞ 49

print(round_number(133, 14))  # ➞ 140
