"""
    Head Recursion - when we call the recursive func 1st and then do our work, its called Head Rec.

"""

def print_1_to_n(n):

    if n == 0:         #base cond
        return

    print_1_to_n(n-1)   #head recursion

    print(n)            #our work

n = int(input("Enter n "))
print_1_to_n(n)

# 2nd Implementation  of generation of list by using recursion

def count_to_n(n):
    """
    Function to return a list of integers from 1 to n using recursion.

    Parameters:
    n (int): The positive integer representing the upper limit of the range.

    Returns:
    list: A list of integers from 1 to n.
    """
    # Your code here
    if n == 0:  # base cond
        return []

    result = count_to_n(n - 1)  # head recursion
    result.append(n)
    return result


n = 5
print(count_to_n(n))