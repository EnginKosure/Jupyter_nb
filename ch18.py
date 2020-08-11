def jumpingOnClouds(c):
    # if len(c) == 1:
    #     return 0

    # if len(c) == 2:
    #     return 1 if c[1] == 0 else 0

    # if c[2] == 0:
    #     return 1 + jumpingOnClouds(c[2:])

    # if c[2] == 1:
    #     return 1 + jumpingOnClouds(c[1:])

    i = 0
    r = 0
    while i < len(c)-1:
        r += 1
        if c[i] == 1:
            i -= 1
        # if i == c.count(1)-1:
        #     break
        i += 2
    return r


a = [0, 0, 1, 0, 0, 1, 0]
d = [0, 0, 0, 0, 1, 0]
e = [0, 0, 0, 0, 0, 0, 0, 1, 0]
f = [0, 0, 0, 1, 0, 0]
print(jumpingOnClouds(a))
print(jumpingOnClouds(d))
print(jumpingOnClouds(e))
print(jumpingOnClouds(f))
