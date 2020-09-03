#[1, 1, 0, 0, 0, 1, 0]
# You free the prisoner in the 1st cell.

#[0, 0, 1, 1, 1, 0, 1]
# You free the prisoner in the 3rd cell (2nd one locked).

#[1, 1, 0, 0, 0, 1, 0]
# You free the prisoner in the 6th cell (3rd, 4th and 5th locked).

#[0, 0, 1, 1, 1, 0, 1]
# You free the prisoner in the 7th cell - and you are done!


def free(l):
    f = 0
    for i in l:
        if i == 1:
            f += 1
            l = [1 if i == 0 else 0 for i in l]
            print(l)
        if i == 0:
            continue

    print(f)
    return f


free([1, 1, 0, 0, 0, 1, 0])  # ➞ 4

free([1, 1, 1])  # ➞ 1

# print(free([0, 0, 0]))  # ➞ 0

# free([0, 1, 1, 1])  # ➞ 0
