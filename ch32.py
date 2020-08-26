# Create a function that takes a string txt and censors any word from a given list
# The text removed must be replaced by the given character char.

import re


def censor_string(s, l, r):
    # for i in s.split():
    #     if i in l:
    #         s = s.replace(i, r*len(i))
    # print(s)
    # return s
    for i in l:
        if ' '+i.lower() in s:
            s = re.sub(i.lower(), r*len(i), s)
    print(s)
    return s


censor_string("Today is a Wednesday!", ["Today", "a"], "-")
# ➞ "----- is - Wednesday!"

# "The *** jumped **** the moon.")
censor_string("The cow jumped over the moon.", ["cow", "over"], "*"),

censor_string("Why did the chicken cross the road?", [
              "Did", "chicken", "road"], "*")  # ➞ "Why *** the ******* cross the ****?"
