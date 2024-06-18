class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        grp = {'I' : 1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        sum = 0
        for i in range(0,len(s)-1):
            if grp[s[i]]>=grp[s[i+1]]:
                sum = sum+grp[s[i]]
            else :
                sum = sum-grp[s[i]]
        return sum+grp[s[-1]]
