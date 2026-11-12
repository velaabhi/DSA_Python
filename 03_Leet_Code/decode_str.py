"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.



Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
"""

s = "3[a2[c]]"


def decodeString(s: str) -> str:

    count_stk = []
    str_stk = []

    curr_num = 0
    curr_str = ""

    for ch in s:

        if ch.isdigit():
            curr_num = curr_num*10 + int(ch)

        elif ch == '[':
            curr_num = int(ch_no)
            count_stk.append(curr_num)

        elif ch.isalpha():
            curr_str = curr_str.join(ch)

        elif ch == ']':
            str_stk.append(curr_num*curr_str)
            curr_str = ""

        else:
            pass

    return str(str_stk)

print(decodeString(s))