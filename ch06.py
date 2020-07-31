# tournament_scores(["A 0 - 1 B", "C 2 - 0 D", "B 2 - 2 C", "D 3 - 1 A", "A 2 - 2 C", "B 2 - 0 D"]) ➞
#[ [ "B", 7, 5, 3 ], [ "C", 5, 6, 2 ], [ "D", 3, 3, -2 ], [ "A", 1, 3, -3 ] ]
# Final order is B, C, D, A. All teams have different points,
# so that a simple descendant sort by points obtained is enough.
#[Team, PT, GS, GD]


def calculate_PT(st):
    PT = {}
    x = st.split(' ')  # ['A', '0', '-', '1', 'B']
    if x[1] > x[3]:
        PT[x[0]] = 3
        PT[x[4]] = 0

    elif x[1] == x[3]:
        PT[x[0]] = 1
        PT[x[4]] = 1
    else:
        PT[x[4]] = 3
        PT[x[0]] = 0
    return PT


calculate_PT("A 0 - 1 B")
y = ["A 0 - 1 B", "C 2 - 0 D", "B 2 - 2 C",
     "D 3 - 1 A", "A 2 - 2 C", "B 2 - 0 D"]
calc_Total = list(map(calculate_PT, y))
print(calc_Total)
#[{'B': 3, 'A': 0}, {'C': 3, 'D': 0}, {'B': 1, 'C': 1}, {'D': 3, 'A': 0}, {'A': 1, 'C': 1}, {'B': 3, 'D': 0}]
for i in calc_Total:
    print(i.items()[0])
