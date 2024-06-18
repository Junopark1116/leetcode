class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        dic = {}
        size = len(nums)
        res = [None]*size
        for i in range(size):
            dic[nums[i]] = i
        nums.sort()
        for i in range(size-1,-1,-1):
            if size-1-i == 0:
                res[dic[nums[i]]] = "Gold Medal"
            elif size-1-i == 1:
                res[dic[nums[i]]] = "Silver Medal"
            elif size-1-i == 2:
                res[dic[nums[i]]] = "Bronze Medal"
            else:
                res[dic[nums[i]]] = str(size-i)
        return res    
