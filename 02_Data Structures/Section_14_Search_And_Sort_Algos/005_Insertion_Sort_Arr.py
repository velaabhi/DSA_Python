import array

"""
    In insertion sort, we always consider the sub arrays in each pass, and the size of these sub arrays
    goes on increasing with each pass. And at the end of each pass we see to it that this current sub array
    has been sorted correctly. 
    
    Note - Here we do shifting of elements, in selection and bubble we did swapping of ele
    
        For eg [25,12,40,35] - so here we will need 3 (size-1) passes as size is 4.
        pass 1 - [25] - always sorted - so we can ignore the very 1st pass
        pass 1 - [25,12] - now we will need to sort this arr, by inserting 12 at correct position and shifting 25 to the right
        pass 2 - [12,25,40] - sorted so no need to sort
        pass 3 - [12,25,40,35] - not sorted, insert 35 at correct position and shift 40 to the right
"""


"""
    In insertion sort, we divide the array into two parts:
        1. A sorted subarray on the left
        2. An unsorted subarray on the right
        
        Initially, the first element is considered sorted.
        In each pass, we take one element from the unsorted part
        and insert it into its correct position in the sorted subarray.
        
        This is done by shifting elements to the right, not by swapping.
        With each pass, the size of the sorted subarray increases by one.

    Pass 1: [25] | [12, 40, 35]
        Insert 12 → shift 25
        Result: [12, 25, 40, 35]
    
    Pass 2: [12, 25] | [40, 35]
        40 already in correct position
        Result: [12, 25, 40, 35]
    
    Pass 3: [12, 25, 40] | [35]
        Insert 35 → shift 40
        Result: [12, 25, 35, 40]

"""

def insertion_sort(arr):
    n = len(arr)

    for currentIndex in range(1,n):  # here we start from 1 bcz we assume that 1st ele i.e. 0th ele is always                                  #sorted
        currentEle = arr[currentIndex]
        correctPosition = currentIndex - 1

        while correctPosition >= 0:
            if (arr[correctPosition] < currentEle):
                break  # break bcz it means that the ele is sorted
            else:
                arr[correctPosition + 1] = arr[correctPosition]  # we shift (not swap)
                correctPosition -= 1  # swap and then adjust the position

            arr[correctPosition + 1] = currentEle

    return arr

arr = array.array('i',[25,12,40,35])
print(insertion_sort(arr))