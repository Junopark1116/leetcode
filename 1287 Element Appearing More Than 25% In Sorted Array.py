from collections import Counter
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        ans = 0
        percent_25_num = int(len(arr) // 4)
        cnt = Counter(arr)
        keys = list(cnt.keys())
        for key in keys:
            if cnt[key] > percent_25_num:
                ans = key
                break  
        return ans
