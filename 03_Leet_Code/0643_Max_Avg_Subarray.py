"""
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
"""
nums = [1,12,-5,-6,50,3]
k = 4

def findMaxAverage(nums: list[int], k: int) -> float:

    left = 0
    rt = k-1
    prefix_sum = 0

    for i in range(k):
        prefix_sum = prefix_sum + nums[i]

    max_sum = prefix_sum

    for rt in range(k-1, len(nums)-1):
        prefix_sum = prefix_sum - nums[left] + nums[rt+1]
        max_sum = max(max_sum, prefix_sum)
        left += 1

    return max_sum/k

print(findMaxAverage(nums,k))
