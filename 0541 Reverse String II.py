class Solution:
    def reverseStr(self, s, k):
        list_s = list(s)
        for s in range(0, len(s), 2*k):
            list_s[s:s+k] = list_s[s:s+k][::-1]
        return "".join(list_s)
