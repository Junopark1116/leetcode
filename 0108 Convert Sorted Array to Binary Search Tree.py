class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def sortToBST(nums):
            if len(nums) == 0:
                return None
            mid = nums[len(nums) // 2]
            root = TreeNode(mid)
            root.left = sortToBST(nums[:len(nums) // 2])
            root.right = sortToBST(nums[len(nums) // 2 + 1:])
            return root
        return sortToBST(nums)
