def getMinimumCost(x, y):
    y.sort(reverse=True)
    return sum([(int(i/x)+1)*y[i] for i in range(len(y))])


c = [1, 3, 5, 7, 9]
k = 3
getMinimumCost(k, c)  # 29
