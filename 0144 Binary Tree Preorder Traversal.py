class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        visit = []
        if root is not None:
            visit.append(root.val)
            visit.extend(self.preorderTraversal(root.left))
            visit.extend(self.preorderTraversal(root.right))
        return visit
