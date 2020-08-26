# Create a function that takes a string txt and censors any word from a given list
# The text removed must be replaced by the given character char.


def censor_string(txt, lst, char):
    res = ""
    aux = txt.split(" ")
    for x in aux:
        if x in lst:
            res = res + " " + char * len(x)
        else:
            res = res + " " + x
    print(res[1:])
    return res[1:]


censor_string("Today is a Wednesday!", ["Today", "a"], "-")
# ➞ "----- is - Wednesday!"

# "The *** jumped **** the moon.")
censor_string("The cow jumped over the moon.", ["cow", "over"], "*"),

censor_string("Why did the chicken cross the road?", [
              "Did", "chicken", "road"], "*")  # ➞ "Why *** the ******* cross the ****?"
