
def sum_of_digits(n):

    if n == 0:
        return 0

    n = n%10
    small_ans = sum_of_digits(n-1)
    ans = n + small_ans

    return ans

n = int(input("Enter n "))
print(sum_of_digits(n))