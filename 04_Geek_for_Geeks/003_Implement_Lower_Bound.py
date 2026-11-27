"""
Implement Lower Bound

Given a sorted array arr[] (following 0-based indexing) and a number target, find the lower bound of the target in this given array.

The lower bound of a number is defined as the smallest index in the sorted array where the element is greater than or equal to the given number.
If all the elements in the given array are smaller than the target, the lower bound will be the length of the array.

Input:  arr[] = [2, 3, 7, 10, 11, 11, 25], target = 9
Output: 3
Explanation: 3 is the smallest index in arr[] where element (arr[3] = 10) is greater than or equal to 9.
"""

arr = [2, 3, 7, 10, 11, 11, 25]
target = 9


def lowerBound(arr, target):
    low = 0
    high = len(arr)

    while low < high:
        mid = (low + high) // 2

        if arr[mid] < target:
            low = mid + 1

        elif arr[mid] >= target:
            high = mid

    return low

print(lowerBound(arr, target))