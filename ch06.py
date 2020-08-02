def tournament_scores(y):
    # tournament_scores(["A 0 - 1 B", "C 2 - 0 D", "B 2 - 2 C", "D 3 - 1 A", "A 2 - 2 C", "B 2 - 0 D"]) ➞
    # [ [ "B", 7, 5, 3 ], [ "C", 5, 6, 2 ], [ "D", 3, 3, -2 ], [ "A", 1, 3, -3 ] ]
    # Final order is B, C, D, A. All teams have different points,
    # so that a simple descendant sort by points obtained is enough.
    # [Team, PT, GS, GD]

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

    def calculate_PAY(st):
        a, _, b, _, _, _, c, _, d = st
        PAY = {}
        PAY[a] = b
        PAY[d] = c
        return PAY

    def calculate_GS(st):
        a, _, b, _, _, _, c, _, d = st
        GS = {}
        GS[a] = int(b)-int(c)
        GS[d] = int(c)-int(b)
        return GS

    # calculate_PT("A 0 - 1 B")
    # y = ["A 0 - 1 B", "C 2 - 0 D", "B 2 - 2 C",
    #     "D 3 - 1 A", "A 2 - 2 C", "B 2 - 0 D"]
    calc_Total = list(map(calculate_PT, y))
    PAY_Total = list(map(calculate_PAY, y))
    GS_Total = list(map(calculate_GS, y))

    print(calc_Total)
    # [{'B': 3, 'A': 0}, {'C': 3, 'D': 0}, {'B': 1, 'C': 1}, {'D': 3, 'A': 0}, {'A': 1, 'C': 1}, {'B': 3, 'D': 0}]
    print(PAY_Total)
    # [{'A': '0', 'B': '1'}, {'C': '2', 'D': '0'}, {'B': '2', 'C': '2'}, {'D': '3', 'A': '1'}, {'A': '2', 'C': '2'}, {'B': '2', 'D': '0'}]
    print('GS_TOTAL', GS_Total)
    cc = [{k: v}
          for k, v in [(k, v) for x in calc_Total for (k, v) in x.items()]]
    # cc [{'B': 3}, {'A': 0}, {'C': 3}, {'D': 0}, {'B': 1}, {'C': 1}, {'D': 3}, {'A': 0}, {'A': 1}, {'C': 1}, {'B': 3}, {'D': 0}]
    print('cc', cc)
    pay_pay = [{k: int(v)}
               for k, v in [(k, v) for x in PAY_Total for (k, v) in x.items()]]
    print('pay_pay', pay_pay)
    # [{'A': 0}, {'B': 1}, {'C': 2}, {'D': 0}, {'B': 2}, {'C': 2}, {'D': 3}, {'A': 1}, {'A': 2}, {'C': 2}, {'B': 2}, {'D': 0}]

    gs_gs = [{k: int(v)}
             for k, v in [(k, v) for x in GS_Total for (k, v) in x.items()]]
    print('gs_gs', gs_gs)

    # print('ff', ff)
    dd = {}
    for i in range(len(cc)):
        print(cc[i])
        if tuple(cc[i].keys()) not in dd:
            dd[tuple(cc[i].keys())] = list(cc[i].values())[0]
        else:
            dd[tuple(cc[i].keys())] += list(cc[i].values())[0]

    print('dd', dd)
    # dd {('B',): 7, ('A',): 1, ('C',): 5, ('D',): 3}

    gg = {}
    for i in range(len(pay_pay)):
        print(pay_pay[i])
        if tuple(pay_pay[i].keys()) not in gg:
            gg[tuple(pay_pay[i].keys())] = list(pay_pay[i].values())[0]
        else:
            gg[tuple(pay_pay[i].keys())] += list(pay_pay[i].values())[0]

    print('gg', gg)
    # gg {('A',): 3, ('B',): 5, ('C',): 6, ('D',): 3}

    gs = {}
    for i in range(len(pay_pay)):
        print(gs_gs[i])
        if tuple(gs_gs[i].keys()) not in gs:
            gs[tuple(gs_gs[i].keys())] = list(gs_gs[i].values())[0]
        else:
            gs[tuple(gs_gs[i].keys())] += list(gs_gs[i].values())[0]

    print('gs', gs)
    # gs {('A',): -3, ('B',): 3, ('C',): 2, ('D',): -2}
    # [Team, PT, GS, GD]
    a1 = ['A', dd[('A',)], gg[('A',)], gs[('A',)]]
    b1 = ['B', dd[('B',)], gg[('B',)], gs[('B',)]]
    c1 = ['C', dd[('C',)], gg[('C',)], gs[('C',)]]
    d1 = ['D', dd[('D',)], gg[('D',)], gs[('D',)]]
    nihai = list([a1, b1, c1, d1])
    sorted_n = sorted(nihai, key=lambda x: (x[1], x[2], x[3]), reverse=True)

    print(nihai)

    print(sorted_n)
    return sorted_n


tournament_scores(["A 2 - 1 B", "C 3 - 0 D", "B 1 - 1 C",
                   "D 1 - 0 A", "A 3 - 0 C", "B 2 - 4 D"])
# [ [ "A", 6, 5, 3 ], [ "D", 6, 5, 0 ], [ "C", 4, 4, 0 ], [ "B", 1, 4, -3 ] ]
# Final order is A, D, C, B (A and D have same points and same number of scored goals, but A has a greater goals difference than D).
