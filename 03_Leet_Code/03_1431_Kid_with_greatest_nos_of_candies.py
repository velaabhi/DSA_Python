class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxmimum = max(candies)
        output = []
        for candy in candies:
            if extraCandies+candy >= maxmimum:
                output.append(True)
            else:
                output.append(False)

        return output