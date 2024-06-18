class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust:
            if n == 1:
                return 1
            else:
                return -1
        rT = [[] for _ in range(n+1)]
        for a, b in trust:
            rT[b].append(a)
        for i in range(1, n+1):
            if len(rT[i]) == n-1:
                for t in range(1, n+1):
                    if i in rT[t]:
                        return -1             
                return i
        return -1
