class Solution:
    def divisorGame(self, n: int) -> bool:
        ans = [False]
        ans.append(False)
        for i in range(2, n+1):
            ans.append(False) 
            for j in range(i-1, 0, -1): 
                if i % j == 0: 
                    if ans[i-j] == False: 
                        ans[i] = True
                        break
        return ans[n]
