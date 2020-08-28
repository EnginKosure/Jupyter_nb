# Create a function that returns the majority vote in a list.
# A majority vote is an element that occurs > N/2 times in a list
# (where N is the length of the list).


def majority_vote(l):
    return sorted(l, key=l.count)[0]


majority_vote(["A", "A", "B"])  # ➞ "A"

majority_vote(["A", "A", "A", "B", "C", "A"])  # ➞ "A"

majority_vote(["A", "B", "B", "A", "C", "C"])  # ➞ None
