import re


def valid_color(s):
    st = s  # Your Hex

    match = re.search(
        r'rgba?\(((25[0-5]|2[0-4]\d|1\d{1,2}|\d\d?)\s*[ \t]?,[ \t]?\s*?){2}(25[0-5]|2[0-4]\d|1\d{1,2}|\d\d?)\s*,?\s*([01]\.?\d*?)?\)', st)
# \bc[ \t]*a[ \t]*t[ \t]*s\b
    return bool(match)


print(valid_color("rgb(0,0,0)"))  # ➞ True

# print(valid_color("rgb(0,,0)"))  # ➞ False

print(valid_color("rgb(255,256,255)"))  # ➞ False

print(valid_color("rgba(0,0,0,0.123456789)"))  # ➞ True
