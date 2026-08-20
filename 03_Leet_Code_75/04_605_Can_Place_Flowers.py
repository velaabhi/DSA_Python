"""
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.



Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false


Constraints:

1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length
"""
from typing import List

flowerbed = [1,0,0,0,1]
n = 1


def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
    size = len(flowerbed)
    counter = 0

    for i in range(0, size):

        if size == 1:
            if flowerbed[0] == 0:
                counter += 1
                flowerbed[0] = 1
            break

        if i == 0:
            if flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                counter += 1

        elif i == size - 1:
            if flowerbed[i - 1] == 0 and flowerbed[i] == 0:
                flowerbed[i] = 1
                counter += 1

        else:
            if flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                counter += 1

    if n <= counter:
        return True
    else:
        return False


print(canPlaceFlowers(flowerbed, n))

