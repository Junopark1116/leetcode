class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        val = []
        def search(root, depth):
            nonlocal val
            if not root:
                return
            if len(val) < depth+1:
                val.append([])
            val[depth].append(root.val)
            search(root.left, depth+1)
            search(root.right, depth+1)   
        search(root, 0)
        ans = [sum(x)/len(x) for x in val] 
        return ans
