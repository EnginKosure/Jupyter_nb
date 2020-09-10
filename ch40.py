# # daily-python-challenge
# QUESTION:
# This is an interview question asked by Amazon.
# Given an integer k and a string s, find the length of the longest substring
# that contains at most k distinct characters.
# For example, given s = "abcba" and k = 2,
# the longest substring with k distinct characters is "bcb".


# def longest(s, k):
#     long = ''
#     for i in range(len(s)):
#         for j in range(i + 1, len(s) + 1):
#             sub = s[i:j]
#             if len(set(sub)) > k:
#                 break
#             if len(sub) > len(long):
#                 long = sub
#     return long

def longest(s, k):
    return sorted([s[i:j] for i in range(len(s)) for j in range(
        i + 1, len(s) + 1) if len(set(list(s[i:j]))) <= k], key=len)[-1]


s = "abcba"
k = 2
print(longest(s, k))
