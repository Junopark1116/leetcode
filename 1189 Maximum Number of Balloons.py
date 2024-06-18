from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        cnt = collections.Counter(text)  
        ballon_key = ["b", "a", "l", "o", "n"]
        for key in ballon_key:
            if key not in list(cnt.keys()):
                return 0
        return min(cnt['b'],cnt['a'],cnt['l']//2,cnt['o']//2,cnt['n'])
