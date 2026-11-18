"""
75. Sort Colors
Medium
Topics
premium lock icon
Companies
Hint
You are given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.



Example 1:

Input: nums = [2,0,2,1,1,0]

Output: [0,0,1,1,2,2]

Explanation:

The array has two 0s, two 1s, and two 2s. Sorting them in-place places all 0s first, then all 1s, then all 2s.
"""

nums = [2,0,2,1,1,0]

def sortColors(nums: list[int]):

    left = 0
    i = 0
    rt = len(nums) - 1

    while i <=  rt:
        if nums[i] == 2:
            nums[i], nums[rt] = nums[rt], nums[i]
            rt -= 1

        elif nums[i] == 1:
            i += 1
        else:
            nums[left], nums[i] = nums[i], nums[left]
            left += 1
            i += 1
    return nums

print(sortColors(nums))