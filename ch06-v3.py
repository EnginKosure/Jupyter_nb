# https://edabit.com/challenge/KETgxWCWtrk7oLM49


def tournament_scores(y):

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

    def calculate_GG(st):
        a, _, b, _, _, _, c, _, d = st
        GG = {}
        GG[a] = b
        GG[d] = c
        return GG

    def calculate_GS(st):
        a, _, b, _, _, _, c, _, d = st
        GS = {}
        GS[a] = int(b)-int(c)
        GS[d] = int(c)-int(b)
        return GS

    calc_Total = list(map(calculate_PT, y))
    GG_Total = list(map(calculate_GG, y))
    GS_Total = list(map(calculate_GS, y))

    cc = [{k: v}
          for k, v in [(k, v) for x in calc_Total for (k, v) in x.items()]]

    def dict_gen(h):
        return [{k: int(v)}
                for k, v in [(k, v) for x in h for (k, v) in x.items()]]
    gg_gg = dict_gen(GG_Total)
    gs_gs = dict_gen(GS_Total)

    def flattener(a):
        dd = {}
        for i in range(len(a)):
            if tuple(a[i].keys()) not in dd:
                dd[tuple(a[i].keys())] = list(a[i].values())[0]
            else:
                dd[tuple(a[i].keys())] += list(a[i].values())[0]
        return dd

    dd = flattener(cc)
    gg = flattener(gg_gg)
    gs = flattener(gs_gs)

    # [Team, PT, GS, GD]
    a1 = ['A', dd[('A',)], gg[('A',)], gs[('A',)]]
    b1 = ['B', dd[('B',)], gg[('B',)], gs[('B',)]]
    c1 = ['C', dd[('C',)], gg[('C',)], gs[('C',)]]
    d1 = ['D', dd[('D',)], gg[('D',)], gs[('D',)]]
    n = list([a1, b1, c1, d1])
    sorted_n = sorted(n, key=lambda x: (x[1], x[2], x[3]), reverse=True)
    print(sorted_n)
    return sorted_n


tournament_scores(["A 2 - 1 B", "C 3 - 0 D", "B 1 - 1 C",
                   "D 1 - 0 A", "A 3 - 0 C", "B 2 - 4 D"])
