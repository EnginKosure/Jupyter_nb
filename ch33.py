# Create a function that returns the majority vote in a list.
# A majority vote is an element that occurs > N/2 times in a list
# (where N is the length of the list).


def majority_vote(l):
    a = sorted([l.count(i) for i in l], reverse=True)
    a = set(a)
    print(a)
    if len(a) == 1:
        return None
    return sorted(l, key=l.count, reverse=True)[0]


print(majority_vote(["A", "A", "B"]))  # ➞ "A"

print(majority_vote(["A", "A", "A", "B", "C", "A"]))  # ➞ "A"

print(majority_vote(["A", "B", "B", "A", "C", "C"]))  # ➞ None
