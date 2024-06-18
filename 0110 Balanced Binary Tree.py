class Solution:
    ans = True
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def dfs(node)->int:
            if not node:
                return -1
            l = dfs(node.left)
            r = dfs(node.right)
            if abs(l -r) > 1:
                self.ans = False
            return max(l, r) + 1
        dfs(root)
        return self.ans
