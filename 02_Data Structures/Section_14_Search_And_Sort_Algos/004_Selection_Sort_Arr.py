import array

"""
   In Selection sort what we do is, we select an element and compare it with the remaining unsorted
   ele(to the right side of that ele). In bubble sort we compare only the adjacent ele and swap
   And if the current index ele is greater than the other index ele, then we just swap the ele.
   eg  [64, 25, 12, 22, 11]
        In pass 1 - we compare 64 with 25 -> greater ->swap [25, 64, 12, 22, 11]
                    we compare 25 with 12 -> greater ->swap [12, 64, 25, 22, 11]
                    we compare 12 with 22 -> smaller ->skip
                    we compare 12 with 11 -> greater ->swap [11, 64, 25, 22, 12 ]
        In pass 2 - since our left most ele got fixed so now in 2nd loop we will 
                    start from the next index hence range (i,size).. and so on
                    
"""

# done by me
def selection_sort(arr):

    size = len(arr)

    for i in range(0,size):

        for j in range(i,size):

            if arr[i]>arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr

arr = array.array('i',[64, 25, 12, 22, 11])

#print(selection_sort(arr))



#Actual code as recommended by course

def actual_sel_sort(in_arr):
    size = len(in_arr)

    # min_index = 0                                               -initially we will take the case with 0 as min_index
    #                                                             -     then update to accomodate all cases by using for
    # for j in range(1,n):                                        - range will always start from next ele for curr ele, cz
    #                                                              -      we have to keep curr ele as is and compare it with others
    #     if in_arr[j] < in_arr[min_index]:                       -finding min ele in the pass
    #         min_index = j                                       -assinging the min_index to the min ele
    #
    # in_arr[0], in_arr[min_index] = in_arr[min_index], in_arr[0]  - swapping

    for i in range(size-1):
        min_index = i

        for j in range(i+1,size):
            print(f"min_index = {min_index}, arr[min_index] = {in_arr[min_index]} \n j = {j}, arr[j] = {in_arr[j]}")
            if in_arr[j] < in_arr[min_index]:
                min_index = j

        print(f"\nAfter for the min_index is {min_index}")
        in_arr[i],in_arr[min_index] = in_arr[min_index], in_arr[i]
        print(f"-----------------------------swapped elements arr is {in_arr} ----------------------------------")

    return in_arr

in_arr = array.array('i',[64, 25, 12, 6, 22, 11])
print(f"input arr is {in_arr}")
print(actual_sel_sort(in_arr))
