class Game:
    def __init__(self, rows=14, cols=18, mines=40):
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.board = [[Cell() for _ in range(self.cols)]
                      for _ in range(self.rows)]
        self.set_mine()
        self.set_position()

    def set_mine(self):
        x = 0
        while x <= self.mines:
            for i in range(self.mines//10):
                for j in range(self.mines//4):
                    self.board[i][j].mine = True
                    self.board[i][j].row = i
                    self.board[i][j].col = j
                    x += 1

    def set_position(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.board[i][j].row = i
                self.board[i][j].col = j

    # all(i.neighbors == sum(b[x][y].mine for x, y in [(i.row+x, i.col+y) for x, y in [(x, y) for x in range(-1, 2) for y in range(-1, 2) if x or y]] if 0 <= x < r and 0 <= y < c) for i in lst)


class Cell:

    def __init__(self):
        self.open = False
        self.mine = False
        self.neighbor = 0
        self.flag = False
        self.row = 0
        self.col = 0


game = Game()
# game.rows ➞ 14
# game.cols ➞ 18
# game.mines ➞ 40


# g1 = (Game(), 14, 18, 40)
# g2 = (Game(20, 20, 20), 20, 20, 20)
# g3 = (Game(20, 20, 300), 20, 20, 300)
# g4 = (Game(25, 25, 200), 25, 25, 200)
# print('---------------------------------')

# for g, r, c, m in [g1, g2, g3, g4]:
#     b = g.board
#     lst = [cell for row in b for cell in row]

#     print('Tests for Game({}, {}, {})'.format(r, c, m))
#     Test.assert_equals(g.rows, r, 'Attribute rows')
#     Test.assert_equals(g.cols, c, 'Attribute cols')
#     Test.assert_equals(g.mines, m, 'Attribute mines')
#     Test.assert_equals(len(b), r, 'Board height')
#     Test.assert_equals(len(b[0]), c, 'Board width')
#     Test.assert_equals(sum(type(i) is Cell for i in lst),
#                        r*c, 'Number of Cells')
#     Test.assert_equals(sum(i.mine for i in lst), m, 'Number of mines')
#     Test.assert_equals(all((b[i][j].row, b[i][j].col) == (
#         i, j) for i in range(r) for j in range(c)), True, 'Positions match')
#     Test.assert_equals(all(not i.flag or i.open for i in lst),
#                        True, 'Attributes flag and open')
#     Test.assert_equals(all(i.neighbors == sum(b[x][y].mine for x, y in [(i.row+x, i.col+y) for x, y in [(
#         x, y) for x in range(-1, 2) for y in range(-1, 2) if x or y]] if 0 <= x < r and 0 <= y < c) for i in lst), True, 'Neighbors')
#     print('---------------------------------')
