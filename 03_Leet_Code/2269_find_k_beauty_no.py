"""
The k-beauty of an integer num is defined as the number of substrings of num when it is read as a string that meet the following conditions:
- It has a length of k.
- It is a divisor of num.
Given integers num and k, return the k-beauty of num.

Note:
- Leading zeros are allowed.
- 0 is not a divisor of any value.
A substring is a contiguous sequence of characters in a string.

Example 1:
Input: num = 240, k = 2 Output: 2 Explanation: The following are the substrings of num of length k: - "24" from "240": 24 is a divisor of 240. - "40" from "240": 40 is a divisor of 240. Therefore, the k-beauty is 2.
Example 2:
Input: num = 430043, k = 2 Output: 2 Explanation: The following are the substrings of num of length k: - "43" from "430043": 43 is a divisor of 430043. - "30" from "430043": 30 is not a divisor of 430043. - "00" from "430043": 0 is not a divisor of 430043. - "04" from "430043": 4 is not a divisor of 430043. - "43" from "430043": 43 is a divisor of 430043. Therefore, the k-beauty is 2. - let me present my brute force - from ex and explanation its clear that we have to move in forward dir only with 2 ele per pass, and with each pass, convert those str ele into int and divide it by whole num by that exptracted k digit no. if remainder ==0, increment count .finally return count - and we have to do it while slidign the window- - act as senior dsa guy, rate my approach, tell me my pluspoints and drawbacks and guide

"""

num = 430043
k = 2
def divisorSubstrings(num: int, k: int) -> int:

    k_beauty_count = 0
    num_str = str(num)
    for left in range(len(num_str)-k+1):
        s1 = int(num_str[left:left+k])
        if s1 != 0 and num % s1 == 0:
            k_beauty_count += 1

    return k_beauty_count

print(divisorSubstrings(num,k))