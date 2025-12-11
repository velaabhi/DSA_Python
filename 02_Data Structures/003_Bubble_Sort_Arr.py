import array

"""
    In bubble sort we do multiple passes of the whole array by comparing current ele with next ele in
    each pass. Here only adjacent elements are compared.
        Then we check if arr[current] > arr[next] then swap
    Now to limit the no of internal iterations what we do is, we subtract the i from the 1st loop in the range of 
    2nd loop, this helps reducing the nos of internal iterations in each pass as i no of ele are already sorted
    in the end and do not req repeated comparisons
    
    After i passes, i elements at the end are already sorted.
    So we don't need to compare them again.
"""

def bubble_sort(arr):
    size = len(arr)

    for i in range(0,size):

        for j in range(0,size-i-1):

            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


    return arr

arr = array.array('i',[64, 34, 25, 12, 22, 11, 90])

print(f"bubble_sorted arr is {bubble_sort(arr)}")