class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        lft=0
        rgt=len(nums)-1
        while lft<=rgt:
            mid=(lft+rgt)//2
            if nums[mid]>target:
                rgt=mid-1
            elif nums[mid]<target:
                lft=mid+1   
            else:
                return mid
        return lft 
