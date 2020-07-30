def uncensor(txt, vowels):
    txt = txt.replace('*', '{}')
    print(txt)
    print(*vowels)
    return txt.format(*vowels)


# ➞ "Where did my vowels go?"
print(uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo"))

# uncensor("abcd", "") ➞ "abcd"

# uncensor("*PP*RC*S*", "UEAE") ➞ "UPPERCASE"
