"""
    1. Recursion is a programming technique in which a function calls itself
       to solve a problem.

    2. It is used when a problem can be broken down into smaller instances
       of the same problem.

    3. Every recursive function must have:
       a) Base case – to stop recursion
       b) Recursive case – where the function calls itself

    4. Recursion uses the call stack (LIFO – Last In, First Out),
       where each function call is pushed onto the stack and
       removed only after its execution is complete.

    5. In Python, the sys module provides:
       - getrecursionlimit()
       - setrecursionlimit()

    In the following code we are going to find the n factorial by using recursion
    Note - factorial of ZERO is 1

    we always go in decreasing order, from n upto 0 or 1 i.e. call the func recursively by passing n-1
    as param
"""

def factorial(n):

    if n == 0:          #base condition
        return 1

    else:
        small_ans = factorial(n-1)      #we go on reducing the n
        ans = n * small_ans

    return ans

n = int(input("Enter a number "))
print(factorial(n))
