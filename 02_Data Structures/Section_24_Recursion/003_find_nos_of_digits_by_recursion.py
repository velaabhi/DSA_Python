"""
    we have to find the nos of digits given in the input number.
    -   here we will use the "division by 10" logic in order to reduce the original no
     and after reducing it we would add 1 to our count
    -   we will have 2 base cases,  1. 1<= n <=9
                                    2. n == 0

"""

def count_digits(n):

    print(f"value of n is {n}")
    if n >= 0 and n <= 9 :
        return 1
    #
    # if n == 0:
    #     return 1

    n = n//10
    small_ans = count_digits(n)
    ans = 1 + small_ans

    return ans

n = int(input("Enter the number "))
print(count_digits(n))