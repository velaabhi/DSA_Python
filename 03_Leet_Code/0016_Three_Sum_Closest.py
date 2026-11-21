"""
You are given an integer array nums of length n and an integer target.

Find three integers at distinct indices in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.



Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""
nums = [-1,2,1,-4]
target = 1

def threeSumClosest(nums: list[int], target: int) -> int:

    nums.sort()
    closest_sum = nums[0] + nums[1] + nums[2]
    for i in range(len(nums)-2):
        left = i+1
        rt = len(nums) - 1

        while left < rt:
            new_sum = nums[i] + nums[left] + nums[rt]

            if target == new_sum:
                return target

            if abs( target - new_sum) < abs(target - closest_sum):
                closest_sum = new_sum

            if new_sum < target:
                left += 1
            else:
                rt -= 1

    return closest_sum
print(threeSumClosest(nums,target))