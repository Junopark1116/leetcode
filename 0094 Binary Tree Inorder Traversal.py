class Solution:    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:     
        output = []
        def dfs(node):
            if node:
                dfs(node.left) 
                output.append(node.val) 
                dfs(node.right)   
        dfs(root)
        return output
