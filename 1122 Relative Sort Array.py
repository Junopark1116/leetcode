from collections import Counter
class Solution:
    def relativeSortArray(self, arr1, arr2):
        tmp1 = []
        tmp2 = []
        cnt = Counter(arr1)
        for num in arr2:
            if num in arr1:
                tmp1 = tmp1 + [num] * cnt[num]
        tmp2 = sorted([num for num in arr1 if num not in arr2 ])
        return tmp1 + tmp2
