class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maximum = 0
        temp = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                temp += 1
            else:
                maximum = max(maximum, temp)
                temp = 0
        return max(maximum, temp)
