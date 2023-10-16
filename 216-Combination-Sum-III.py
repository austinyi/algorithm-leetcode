class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans =[]
        def combination(start, k, n, cur):
            if k < 0 or n < 0:
                return
            elif k == 0 and n == 0:
                ans.append(cur)
            else:
                for i in range(start, 10):
                    if n-i >= 0:
                        combination(i+1, k-1, n-i, cur + [i])
        combination(1, k, n, [])
        return ans
        
