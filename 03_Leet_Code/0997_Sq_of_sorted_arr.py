"""
977. Squares of a Sorted Array
Easy
Topics
premium lock icon
Companies
Given an integer array nums sorted in non-decreasing order,
return an array of the squares of each number sorted in non-decreasing order.

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
"""
nums = [-4,-1,0,3,10]

def sortedSquares(nums: list[int]) -> list[int]:

    left = 0
    rt = len(nums) - 1
    last_pos = len(nums) - 1
    l1 = [0] * len(nums)
    while left <= rt:

        if abs(nums[left]) >  abs(nums[rt]) :
            l1[last_pos] = nums[left] ** 2
            left += 1
        else:
            l1[last_pos] = nums[rt] ** 2
            rt -= 1
        last_pos -= 1
    return l1
print(sortedSquares(nums))