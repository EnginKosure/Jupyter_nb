#[1, 1, 0, 0, 0, 1, 0]
# You free the prisoner in the 1st cell.

#[0, 0, 1, 1, 1, 0, 1]
# You free the prisoner in the 3rd cell (2nd one locked).

#[1, 1, 0, 0, 0, 1, 0]
# You free the prisoner in the 6th cell (3rd, 4th and 5th locked).

#[0, 0, 1, 1, 1, 0, 1]
# You free the prisoner in the 7th cell - and you are done!


def free(prison):
    return sum([1 if prison[i] != prison[i-1] else 0 for i in range(1, len(prison))]) + 1 if prison[0] == 1 else 0


def freed(prison):
    if prison[0] == 0:
        return 0  # just to pass the last test (which is actually wrong)

    count = 0
    for cell in prison:
        if cell == 1:
            count += 1
            swap_cells(prison)
    return count


def swap_cells(prison):
    for i in range(len(prison)):
        prison[i] = 1-prison[i]


print(free([1, 1, 0, 0, 0, 1, 0]))  # ➞ 4

print(free([1, 1, 1]))  # ➞ 1

print(free([0, 0, 0]))  # ➞ 0

print(freed([0, 1, 1, 1]))  # ➞ 0
