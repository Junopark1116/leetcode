class Solution:
    def longestPalindrome(self, s: str) -> int:
        ans = 0
        alpha = {}
        for c in s:
            if c not in alpha:
                alpha[c] = 1
            else:
                alpha[c] += 1
        odd_exist = False
        max_odd = 0
        for value in  alpha.values():
            if value % 2 == 0:
                ans += value
            else:
                max_odd = max(max_odd,value)
                odd_exist = True
                ans += ( value -1 )
        if odd_exist:
            ans += 1
        return ans
