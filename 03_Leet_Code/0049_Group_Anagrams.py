"""49. Group Anagrams
Medium
Topics
premium lock icon
Companies
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
Example 1:
initiate an empty list of list [[]]

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]
"""

strs = ["eat","tea","tan","ate","nat","bat"]
def groupAnagrams(strs: list[str]) -> list[list[str]]:

    group = {}
    for word in strs:
        freq_map = {}
        for char in word:
            freq_map[char] = freq_map.get(char, 0) + 1

        key = tuple(sorted(freq_map.items()))
        group.setdefault(key, []).append(word)

    return list(group.values())

print(groupAnagrams(strs))


#alternate
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            key = "".join(sorted(word))

            if key not in groups:
                groups[key] = []
            groups[key].append(word)
        return list(groups.values())