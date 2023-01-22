class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False

        target = total // 2
        
        s = set([0])
        for n in nums:
            c = set()
            for e in s:
                if e + n == target:
                    return True
                c.add(e)
                c.add(e + n)
            s = c
            
        return False
        
