"""
You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part. For example, the string "ababcc" can be partitioned into ["abab", "cc"], but partitions such as ["aba", "bcc"] or ["ab", "ab", "cc"] are invalid.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

Return a list of integers representing the size of these parts.



Example 1:

Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
"""

s = "ababcbacadefegdehijhklij"

def partitionLabels(s: str) -> list[int]:

    occurance_pos = {}
    for i in range (len(s)):
        occurance_pos[s[i]] = i

    part_start = 0
    part_end = 0

    result = []

    for i in range (len(s)):
        last_index = occurance_pos[s[i]]
        part_end = max(last_index,part_end)

        if i == part_end:
            result.append(part_end - part_start + 1)
            part_start = i + 1

    return result

print(partitionLabels(s))