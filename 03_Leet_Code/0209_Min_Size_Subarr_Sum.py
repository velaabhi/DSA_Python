"""
Given an array of positive integers nums and a positive integer target,
return the minimal length of a subarray whose sum is greater than or equal to target.
If there is no such subarray, return 0 instead.

Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0


Constraints:

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 104


Follow up: If you have figured out the O(n) solution,
try coding another solution of which the time complexity is O(n log(n)).
"""

target = 7
nums = [2,3,1,2,4,3]

def minSubArrayLen(target: int, nums: list[int]) -> int:

    subarray_len = float('inf')
    left = 0
    rt = 1
    curr_sum = 0

    while rt < len(nums):
        curr_sum = nums[left] + nums[rt]
        if curr_sum >= target:
            subarray_len = min(subarray_len, len(nums[left, rt]))
        rt += 1


    pass

nums = [2,3,1,2,4,3]
print(minSubArrayLen(target, nums))