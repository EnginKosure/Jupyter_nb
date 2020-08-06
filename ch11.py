# def tic_tac_toe(lst):
#     if lst[0][0] == lst[1][0] == lst[2][0]:
#         return lst[0][0]
#     elif lst[0][1] == lst[1][1] == lst[2][1]:
#         return lst[0][1]
#     elif lst[0][2] == lst[1][2] == lst[2][2]:
#         return lst[0][2]
#     elif lst[0][0] == lst[1][1] == lst[2][2]:
#         return lst[0][0]
#     elif lst[0][2] == lst[1][1] == lst[2][0]:
#         return lst[0][2]
#     for i in lst:
#         if i[0] == i[1] == i[2]:
#             return i[0]
#     else:
#         return 'Draw'


# def tic_tac_toe(board):
#     for i in board:
#         if len(set(i)) == 1:
#             return i[0]
#     for i in list(zip(*board)):
#         print('ZIP', i)
#         if len(set(i)) == 1:
#             return i[0]
#     if len({board[i][i] for i in range(3)}) == 1:
#         return board[0][0]
#     if len({board[i][2-i] for i in range(3)}) == 1:
#         return board[0][2]
#     return 'Draw'


def tic_tac_toe(board):
    d1, d2 = [], []
    for i in range(3):
        col = [board[0][i], board[1][i], board[2][i]]
        if board[i].count('X') == 3 or col.count('X') == 3:
            return 'X'
        if board[i].count('O') == 3 or col.count('O') == 3:
            return 'O'
        d1 += [board[i][i]]
        d2 += [board[i][2-i]]
    if len(set(d2)) == 1:
        return 'X'
    if d1.count('O') == 3:
        return 'O'
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
