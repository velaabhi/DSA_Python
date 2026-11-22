"""
A string is good if there are no repeated characters.

Given a string s​​​​​, return the number of good substrings of length three in s​​​​​​.

Note that if there are multiple occurrences of the same substring, every occurrence should be counted.

A substring is a contiguous sequence of characters in a string.
Example 1:

Input: s = "xyzzaz"
Output: 1
Explanation: There are 4 substrings of size 3: "xyz", "yzz", "zza", and "zaz".
The only good substring of length 3 is "xyz".
"""

s = "xyzzaz"

def countGoodSubstrings(s: str) -> int:
    freq_map = {}
    count = 0
    k = 3

    for i in range(k):
        freq_map[s[i]] = freq_map.get(s[i], 0 )+1

    if len(freq_map) == k:
        count += 1

    for left in range(len(s) - k):
        freq_map[s[left]] = freq_map.get(s[left],0) -1
        freq_map[s[left+k]] = freq_map.get(s[left+k],0) +1

        if freq_map[s[left]] == 0:
            del freq_map[s[left]]
        if len(freq_map) == k:
            count += 1

    return count



def countGoodSubstrings_1(s: str) -> int:

    count = 0
    k = 3

    for left in range(len(s)- k + 1):
        if len((set(s[left:left+k]))) == k:
            count += 1

    return count

print(countGoodSubstrings(s))