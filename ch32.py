# Create a function that takes a string txt and censors any word from a given list
# lst. The text removed must be replaced by the given character char.

# ➞ "----- is - Wednesday!"
censor_string("Today is a Wednesday!", ["Today", "a"], "-")

# "The *** jumped **** the moon.")
censor_string("The cow jumped over the moon.", ["cow", "over"], "*"),

censor_string("Why did the chicken cross the road?", [
              "Did", "chicken", "road"], "*")  # ➞ "Why *** the ******* cross the ****?"
