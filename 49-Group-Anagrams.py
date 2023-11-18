class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana = {}
        for s in strs:
            s_sort = ''.join(sorted(s))
            if s_sort in ana:
                ana[s_sort].append(s)
            else:
                ana[s_sort] = [s]
        return list(ana.values())

