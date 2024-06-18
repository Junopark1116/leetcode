class Solution:
    ans = sys.maxsize
    prev = -sys.maxsize
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        if root.left:
            self.minDiffInBST(root.left)
        self.ans = min(self.ans, root.val - self.prev)
        self.prev = root.val
        if root.right:
            self.minDiffInBST(root.right)
        return self.ans
