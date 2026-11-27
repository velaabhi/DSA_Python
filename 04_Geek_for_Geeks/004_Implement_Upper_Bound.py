"""
Given a sorted array arr[] and a number target, the task is to find the upper bound of the target in this given array.

The upper bound is the smallest index in the sorted array where the element is greater than the given target.
If all the elements in the given array are smaller than or equal to the target, the upper bound will be the length of the array.
Examples :

Input: arr[] = [2, 3, 7, 10, 11, 11, 25], target = 9
Output: 3
Explanation: 3 is the smallest index in arr[], at which element (arr[3] = 10) is larger than 9.
"""
arr = [2, 3, 7, 10, 11, 11, 25]
target = 9

def upperBound(arr, target):
    low = 0
    high = len(arr)

    while low < high:
        mid = (low + high) // 2

        if arr[mid] <= target:
            low = mid + 1

        elif arr[mid] > target:
            high = mid

    return low


print(upperBound(arr, target))