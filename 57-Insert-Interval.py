'''
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new = []
        n = len(intervals)
        i = 0
        while i < n and intervals[i][1] < newInterval[0]:
            new.append(intervals[i])
            i += 1

        if i == n:
            new.append(newInterval)
            return new
        #if intervals[i][0] >= newInterval[0]:
        j = i
        while j < n and intervals[j][0] <= newInterval[1]:
            j+=1
        if j == i:
            new.append([min(newInterval[0],intervals[i][0]), newInterval[1]])
        else:
            new.append([min(newInterval[0],intervals[i][0]), max(newInterval[1],intervals[j-1][1])])
        
        #if j<n:
        for k in range(j,n):
            print(intervals[k:])
            new.append(intervals[k:][0])
        
        return new
 '''
 
 class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = -1
        sig = 1
        if intervals == []:
            res.append(newInterval)
            return res
        
        for i, (a, b) in enumerate(intervals):
            if b < newInterval[0]:
                res.append([a,b])
            elif a > newInterval[1]:
                res.append(newInterval)
                sig = 0
                i -= 1
                break
            else:
                newInterval[0] = min(a, newInterval[0])
                newInterval[1] = max(b, newInterval[1])
        if sig != 0:
            res.append(newInterval)

        return res + intervals[i+1:]
        
