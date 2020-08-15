def last_name_lensort(lst):
    return sorted(lst, key=lambda i: (len(i.split(' ')[1]), i.split(' ')[1]))

#sorted(inputlist, key=lambda e: (len(e[0]), e[0], e[1]))


print(last_name_lensort([
    "Jennifer Figueroa",
    "Heather Mcgee",
    "Amanda Schwartz",
    "Nicole Yoder",
    "Melissa Hoffman"
]))
# ➞ ["Heather Mcgee", "Nicole Yoder", "Melissa Hoffman", "Jennifer Figueroa", "Amanda Schwartz"]
