class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        d = collections.defaultdict(list)
        for w in wordList:
            for i in range(len(w)):
                pattern = w[:i] + "." + w[i+1:]
                d[pattern].append(w)

        q = collections.deque([beginWord])
        visit = set([beginWord])
        ans = 1

        while q:
            for i in range(len(q)):
                w = q.popleft()
                if w == endWord:
                    return ans
                for j in range(len(w)):
                    pattern = w[:j] + "." + w[j+1:]
                    for neigh in d[pattern]:
                        if neigh not in visit:
                            q.append(neigh)
                            visit.add(neigh)
            ans += 1
        return 0
