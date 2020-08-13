# Shiritori Game
# First character of next word must match last character of previous word.
# The word must not have already been said.


class Shiritori:
    def __init__(self):
        self.game_over = False
        self.words = []

    def play(self, word):
        if len(self.words) == 0 or self.words[-1][-1] == word[0] and word not in self.words:
            self.words.append(word)
            return self.words
        self.game_over = True
        return 'game over'

    def restart(self):
        self.words = []
        self.game_over = False
        return 'game restarted'


my_shiritori = Shiritori()

print(my_shiritori.play("apple"))  # ➞ ["apple"]
print(my_shiritori.play("ear"))  # ➞ ["apple", "ear"]
print(my_shiritori.play("rhino"))  # ➞ ["apple", "ear", "rhino"]
print(my_shiritori.play("corn"))  # ➞ "game over"

# Corn does not start with an "o".

print(my_shiritori.words)  # ➞  ["apple", "ear", "rhino"]

# Words should be accessible.

print(my_shiritori.restart())  # ➞ "game restarted"
print(my_shiritori.words)  # ➞ []

# Words list should be set back to empty.

print(my_shiritori.play("hostess"))  # ➞ ["hostess"]
print(my_shiritori.play("stash"))  # ➞ ["hostess", "stash"]
print(my_shiritori.play("hostess"))  # ➞ "game over"
