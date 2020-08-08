import string
x = string.ascii_lowercase
print(x)  # 'abcdefghijklmnopqrstuvwxyz'
y = list(map(chr, range(97, 123)))
print(y)  # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
z = list(map(chr, range(ord('a'), ord('z')+1)))
print(z)
