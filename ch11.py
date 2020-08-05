def tic_tac_toe(lst):
    if lst[0][0] == lst[1][0] == lst[2][0]:
        return lst[0][0]
    elif lst[0][1] == lst[1][1] == lst[2][1]:
        return lst[0][1]
    elif lst[0][2] == lst[1][2] == lst[2][2]:
        return lst[0][2]
    elif lst[0][0] == lst[1][1] == lst[2][2]:
        return lst[0][0]
    elif lst[0][2] == lst[1][1] == lst[2][0]:
        return lst[0][2]
    for i in lst:
        if i[0] == i[1] == i[2]:
            return i[0]
    else:
        return 'Draw'


print(tic_tac_toe([
    ["X", "O", "X"],
    ["O", "X",  "O"],
    ["O", "X",  "X"]
]))  # ➞ "X"

print(tic_tac_toe([
    ["O", "O", "O"],
    ["O", "X", "X"],
    ["E", "X", "X"]
]))
print(tic_tac_toe([
    ["X", "X", "O"],
    ["O", "O", "X"],
    ["X", "X", "O"]
]))
