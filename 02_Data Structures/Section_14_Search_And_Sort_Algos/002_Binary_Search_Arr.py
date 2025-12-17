import array

"""
    Here the most imp pre-cond is that the array is a SORTED (Ascending Order) one. - 
    cal mid inside while loop and do floor div
    1. Find the mid - and compare target with the mid ele
    2. If the target > mid ele change the start to mid+1 and again recal the mid
    3. If the target == mid ele, return that index
    4. If the target < mid ele, change the end to mid-1 and again recal the mid

"""

def binary_search(arr, target):
    
    start, end = 0, len(arr)-1

    while(start <= end):
        mid = (start + end) // 2

        if(arr[mid] == target):
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1


    return -1

arr = array.array('i',[10,23,30,45,50,76,80])
target = 45

print(binary_search(arr,target))