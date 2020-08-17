def valid_color(s):
    return s[:3] == 'rgb' or s[:4] == 'rgba' and eval(0 <= s[5] <= 255)


print(valid_color("rgb(0,0,0)"))  # ➞ True

valid_color("rgb(0,,0)")  # ➞ False

valid_color("rgb(255,256,255)")  # ➞ False

valid_color("rgba(0,0,0,0.123456789)")  # ➞ True
