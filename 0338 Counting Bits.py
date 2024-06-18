class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0]
        for i in range(1, n+1):
            dp.append(dp[i&(i-1)]+1)
        return dp