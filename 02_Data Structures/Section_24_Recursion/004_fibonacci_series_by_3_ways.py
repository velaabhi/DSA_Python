"""
    [0,1,1,2,3,5,8,13,...] is the fibonacci seq and the 0,1 are the base conditions
    while Fn = F(n-1) + F(n-2) is the PMI or recurrence equation
"""


# Implementation 1 - Time complexity is 2^n cz of recursive call and limits till n = 35 to 45
def fibonacci_seq(n):

    if n == 0:
        return 0
    if n == 1:
        return 1

    last_ele = fibonacci_seq(n-1)
    second_last_ele = fibonacci_seq(n-2)

    next_ele = last_ele + second_last_ele

    return next_ele

# n = int(input("Enter the n "))
# print(fibonacci_seq(n))



# Implementation 2 - To improve the time and space complexity we use swapping concept by iteration
#                    (instead of func recursion) and here time comp- O(n) and space comp - O(1)
def fib_by_iteration(n1):

    a,b = 0,1

    for _ in range(n1):
        print(a, end=" ")
        a, b = b, a+b

# n1 = int(input("Enter the n "))
# fib_by_iteration(n1)

#Implementation 3 - Constant time by Binets formula
"""
Binet’s Formula (Constant Time)
    𝐹(𝑛)  = (𝜙^𝑛 - 𝜓^𝑛) / sqrt(5)
    where   𝜙 = (1 + sqrt(5)) / 2  Golden ratio 
            𝜓 = (1 - sqrt(5)) / 2
    
"""
import math

def fibonacci_binet(n):
    phi = (1 + math.sqrt(5)) / 2
    psi = (1 - math.sqrt(5)) / 2
    return round((phi**n - psi**n) / math.sqrt(5))

n = int(input("Enter n: "))
print(fibonacci_binet(n))
