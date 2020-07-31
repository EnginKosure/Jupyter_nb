def first_before_second(r, f, s):
    rlst = r.split(f)
    print(rlst)
    for i in range(len(rlst)-1):
        if rlst[i].count(s) > 0:
            print(False)
            return False
    print(True)
    return True


first_before_second("a rabbit jumps joyfully", "a", "j")  # ➞ True
# Every instance of "a" occurs before every instance of "j".
# print(first_before_second("knaves knew about waterfalls", "k", "w"))


first_before_second("happy birthday", "a", "y")
