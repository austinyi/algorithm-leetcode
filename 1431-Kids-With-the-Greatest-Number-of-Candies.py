class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m = max(candies)
        result = []
        for c in candies:
            if c + extraCandies >= m:
                result.append(True)
            else:
                result.append(False)
        return result
