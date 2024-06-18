class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        len_s = len(s)
        if len_s == 0:
            return True
        cnt = 0
        for val in t:
            if val == s[cnt]:
                cnt = cnt + 1
                if cnt == len_s:
                    return True
                    break
        return False
