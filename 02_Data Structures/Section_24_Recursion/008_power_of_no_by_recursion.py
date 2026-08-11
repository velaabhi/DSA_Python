"""
    To find the power of a no by using recursion.
    x^y

"""

def power_of_no(x,y):

    if y == 0:
        return 1

    if y == 1:
        return x

    y = y-1
    small_ans = power_of_no(x,y)
    ans = x*small_ans

    return ans

x = int(input("Enter x - "))
y = int(input("Enter y - "))

print(f"value of x^y is {power_of_no(x,y)}")


#Optimized version

def power_of_no_optimised(x,y):

    if y == 0:
        return 1

    return x * power_of_no_optimised(x, y-1)

x1 = int(input("Enter x - "))
y1 = int(input("Enter y - "))

print(f"Optimised version - value of x^y is {power_of_no_optimised(x,y)}")
# The optimised version is only code level optimization,
# but it still takes O(y) in time and space complexity

#Following is the most optimised version by using "half multiplication method"
# Here time and space complexity becomes O(log y)
def power_of_no_half(x, y):
    if y == 0:
        return 1

    half = power_of_no(x, y // 2)

    if y % 2 == 0:
        return half * half
    else:
        return x * half * half



