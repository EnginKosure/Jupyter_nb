def amplify(num):
    return [x*10 if x % 4 == 0 else x for x in range(1, num+1)]
