class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]: 
        def dfs(node, path):
            path += '->'
            path += str(node.val)
            if not node.left and not node.right:
                return ans.append(path[2:])
            if node.left:
                dfs(node.left, path)
            if node.right:
                dfs(node.right, path)  
        ans = []
        dfs(root, "")
        return ans
