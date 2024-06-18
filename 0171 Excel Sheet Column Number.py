class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        N = len(columnTitle)
        for n in range(N-1, -1, -1):
            ans += 26**n * (ord(columnTitle[N-n-1])-ord('A')+1)
        return ans
