def amplify(num):
    return [x if x % 4 else x*10 for x in range(1, num+1)]
# Create a function that counts how many characters make up a rectangular shape.
# You will be given a list of strings.


def count_characters(lst):
    return sum(len(i) for i in lst)


print(count_characters([
    "###",
    "###",
    "###"
]))  # ➞ 9

print(count_characters([
    "22222222",
    "22222222",
]))
