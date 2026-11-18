"""
242. Valid Anagram
Easy
Topics
premium lock icon
Companies
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false
"""

s = "anagram"
t = "nagaram"
def isAnagram(s: str, t: str) -> bool:

    if len(s) == len(t):

        freq_map = {}

        for char in s:
            freq_map[char] = freq_map.get(char, 0) + 1

        for char in t:
            if char in freq_map:
                freq_map[char] = freq_map.get(char) - 1
                if freq_map[char] == -1:
                    return False
            else:
                return False

        else:
            return True
    else:
        return False


"""
def isAnagram(s: str, t: str) -> bool:

    if len(s) != len(t):
        return False

    freq_map = {}

    for char in s:
        freq_map[char] = freq_map.get(char, 0) + 1

    for char in t:
        if freq_map.get(char, 0) == 0:
            return False

        freq_map[char] -= 1

    return True
"""



print(isAnagram(s,t))