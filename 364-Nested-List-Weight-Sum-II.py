# My solution
# Testcase 26 is wrong in Leetcode

class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:

        def nestedsum(l):
            unweighted = 0
            weighted = 0
            depth = 1
            for i in l:
                if i.isInteger():
                    unweighted += i.getInteger()
                    weighted += i.getInteger()
                else:
                    unw, w, dep = nestedsum(i.getList())
                    depth = max(depth, dep + 1)
                    unweighted += unw
                    weighted += unw + w
            return unweighted, weighted, depth
        unw, w, d = nestedsum(nestedList)

        return unw * (d + 1) - w
   


'''
### https://leetcode.com/problems/nested-list-weight-sum-ii/solutions/237372/simple-dfs-python-beat-100/?languageTags=python
def depthSumInverse(self, nestedList):
	"""
	:type nestedList: List[NestedInteger]
	:rtype: int
	"""
	self.max_h = 0
	res = []  # (depth, val)

	def dfs(node, depth):
		if not node:
			return
		self.max_h = max(self.max_h, depth)
		if not node.isInteger():
			n_d = depth+1
			for n_i in node.getList():
				dfs(n_i, n_d)
		else:
			res.append((depth, node.getInteger()))

	for node in nestedList:
		dfs(node, 0)
	w = 0
	for dep, val in res:
		w += (self.max_h-dep+1) * val
	return w
'''
