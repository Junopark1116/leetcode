class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        x = 0
        for c in s+t:
            x ^= ord(c) 
        return chr(x)
