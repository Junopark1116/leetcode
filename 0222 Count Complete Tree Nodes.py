def count(root: Optional[TreeNode]):
    if root == None: return 0;
    return count(root.left) + count(root.right) + 1
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        return count(root)
