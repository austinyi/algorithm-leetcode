class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        cur = 0

        i = 0
        if flowerbed[0] == 0:
            while i < len(flowerbed) and flowerbed[i] == 0:
                i += 1
            if i < len(flowerbed):
                n -= i // 2
            else:
                n -= (i+1) // 2

        for f in flowerbed[i:]:
            if f == 1:
                if cur > 0:       
                    n -= (cur - 1) // 2
                if n <= 0:
                    return True
                cur = 0
            else:
                cur += 1
        
        if cur > 0:
            n -= cur // 2
 
        return True if n <= 0 else False
                
