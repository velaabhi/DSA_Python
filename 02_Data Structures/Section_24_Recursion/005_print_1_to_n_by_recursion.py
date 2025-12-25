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