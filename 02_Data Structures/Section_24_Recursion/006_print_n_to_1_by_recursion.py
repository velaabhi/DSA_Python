"""
    Tail Recursion - when we call the recursive func after our work, its called Tail Rec.

"""

def print_1_to_n(n):

    if n == 0:         #base cond
        return

    print(n)            #our work

    print_1_to_n(n-1)   #tail recursion

n = int(input("Enter n "))
print_1_to_n(n)



# 2nd implementation - creating list by using extend func in recursion

def count_down(n):
    """
    Function to return a list of integers from n to 1 using recursion.

    Parameters:
    n (int): The positive integer representing the starting point of the range.

    Returns:
    list: A list of integers from n to 1.
    """
    result = []
    # Your code here
    if n == 0:
        return []

    result = [n]
    result.extend(count_down(n - 1))
    return result


n = 5
count_down(n)