class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        ans = ""
        i = 0

        while i < len(s):
            if i in indices and s[i:].startswith(sources[indices.index(i)]):
                ans += targets[indices.index(i)]
                i += len(sources[indices.index(i)])
            else:
                ans += s[i]
                i += 1
        return ans
        

class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        ans = list(s)

        for i, src, targ in zip(indices, sources, targets):
            if s[i:].startswith(src):
                ans[i] = targ
                for k in range(1, len(src)):
                    ans[i+k] = ""
        
        return "".join(ans)
