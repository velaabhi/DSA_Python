import array

"""
	In linear search we use the Arr, its size and a for loop to check 
    continuously the target with each ele of arr. 
"""


def linear_search(arr, target):
    size = len(arr)
    
    for i in range(size):
        if arr[i] == target:
            return i
    return -1

arr = array.array('i', [1, 2, 3, 4, 5])
target = 4

print(linear_search(arr, target))
