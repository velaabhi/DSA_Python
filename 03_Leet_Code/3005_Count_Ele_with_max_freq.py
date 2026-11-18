"""
3005. Count Elements With Maximum Frequency
You are given an array nums consisting of positive integers.

Return the total frequencies of elements in nums such that those elements all have the maximum frequency.

The frequency of an element is the number of occurrences of that element in the array.

Example 1:

Input: nums = [1,2,2,3,1,4]
Output: 4
Explanation: The elements 1 and 2 have a frequency of 2 which is the maximum frequency in the array.
So the number of elements in the array with maximum frequency is 4.
"""
from typing import List

nums = [1,2,2,3,1,4]

def maxFrequencyElements(nums: List[int]) -> int:
    freq = {}

    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    values = freq.values()

    max_freq = max(values)

    total = 0
    for val in values:
        if val == max_freq:
            total += val

    return total