"""
Equilibrium Point
Difficulty: EasyAccuracy: 28.13%Submissions: 772K+Points: 2Average Time: 15m
Given an array of integers arr[], the task is to find the first equilibrium point in the array.

The equilibrium point in an array is an index (0-based indexing) such that the sum of all elements before that index is the same as the sum of elements after it. Return -1 if no such point exists.

Examples:

Input: arr[] = [1, 2, 0, 3]
Output: 2
Explanation: The sum of left of index 2 is 1 + 2 = 3 and sum on right of index 2 is 3.
Input: arr[] = [1, 1, 1, 1]
Output: -1
Explanation: There is no equilibrium index in the array.
Input: arr[] = [-7, 1, 5, 2, -4, 3, 0]
Output: 3
Explanation: The sum of left of index 3 is -7 + 1 + 5 = -1 and sum on right of index 3 is -4 + 3 + 0 = -1.
"""


# Brute force approach
arr = [1, 2, 0, 3]
def findEquilibrium_brute(arr):

    prefix_sum = [0 for i in range(len(arr))]
    suffix_sum = [0 for i in range(len(arr))]

    prefix_sum[0] = arr[0]
    for i in range(1, len(arr)):
        prefix_sum[i] = prefix_sum[i-1]+arr[i]

    # arr = [1, 2, 0, 3]
    # suff = [6,5,3,3] -> [-4,-3,-2,-1]

    suffix_sum[-1] = arr[-1]
    for i in range(-2, -len(arr)-1, -1):
        print(f"{suffix_sum[i]} = {suffix_sum[i+1]} + {arr[i]}")
        suffix_sum[i] = suffix_sum[i+1]+arr[i]

    print(f"prefix_sum : {prefix_sum}")
    print(f"suffix_sum : {suffix_sum}")

    for i in range(0,len(arr)):

        if prefix_sum[0] == suffix_sum[1]:
            return 0

        if prefix_sum[i-1] == suffix_sum[i+1]:
            return i

    else:
        return -1

# print(findEquilibrium_brute(arr))


# Optimized
arr = [1, 2, 0, 3]
def findEquilibrium(arr):

    total_sum = 0
    for _ in range(len(arr)):
        total_sum += arr[_]

    left_total = 0
    for i in range(len(arr)):

        right_total = total_sum - left_total - arr[i]
        if left_total == right_total:
            return i

        left_total = left_total + arr[i]

    return -1

print(findEquilibrium(arr))


