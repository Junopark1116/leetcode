class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        ans = 0
        nums.sort()
        for i in nums[0::2]: 
            ans += i
        return ans
