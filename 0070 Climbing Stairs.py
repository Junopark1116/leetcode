class Solution:
    def climbStairs(self, n: int) -> int:
        grp = [1, 1]
        for step in range(2, n+1):
            grp.append(grp[step-2] + grp[step-1])    
        return grp[n]
