"""
3090. Maximum Length Substring With Two Occurrences

Given a string s, return the maximum length of a substring such that
it contains at most two occurrences of each character.


Example 1:

Input: s = "bcbbbcba"

Output: 4

Explanation:

The following substring has a length of 4 and contains at most two occurrences of each character: "bcbbbcba".
"""

s = "bcbbbcba"
def maximumLengthSubstring(s: str) -> int:
    freq_map = {}
    left = 0
    max_len = 0

    for rt in range(len(s)):
        freq_map[s[rt]] = freq_map.get(s[rt], 0) + 1

        while freq_map[s[rt]] > 2:
            freq_map[s[left]] -= 1
            left += 1

        max_len = max(max_len, rt-left+1)

    return max_len


print(maximumLengthSubstring(s))


a = [10, 20, 30]
b = a.copy()
b[0] = 100

print(a)
print(b)

------
functions = []

for i in range(3):
    functions.append(lambda: i)

print([f() for f in functions])

--------------

def numbers():
    for i in range(3):
        yield i

gen = numbers()

print(next(gen))
print(next(gen))
print(list(gen))

