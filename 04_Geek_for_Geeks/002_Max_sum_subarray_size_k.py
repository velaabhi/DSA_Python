"""
Given an array of integers arr[]  and a number k. Return the maximum sum of a subarray of size k.

Note: A subarray is a contiguous part of any given array.

Examples:

Input: arr[] = [100, 200, 300, 400], k = 2
Output: 700
Explanation: arr2 + arr3 = 700, which is maximum.
"""

arr = [100, 200, 300, 400]
k = 2

def maxSubarraySum(arr, k):

    left = 0
    rt = k-1
    prefix_sum = 0

    for i in range(0,k):
        prefix_sum = prefix_sum + arr[i]

    max_sum = prefix_sum

    for rt in range(k-1, len(arr)-1):
        prefix_sum = prefix_sum - arr[left] + arr[rt+1]
        max_sum = max(max_sum, prefix_sum)
        left += 1

    return max_sum

print(maxSubarraySum(arr, k))

