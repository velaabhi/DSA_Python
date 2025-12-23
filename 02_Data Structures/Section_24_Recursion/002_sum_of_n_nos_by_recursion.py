"""
    Accept n from user and find out the sum from 1 to n by using the recursion concept

    for n = 0, sum = 0
"""

def sum_of_n(n):

    if n == 0:
        return 0
    if n == 1:
        return 1

    small_ans = sum_of_n(n-1)
    ans = n + small_ans

    return ans

n = int(input("Enter the value of n "))
print(sum_of_n(n))
