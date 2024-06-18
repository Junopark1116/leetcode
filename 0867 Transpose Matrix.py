class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        H, W = len(matrix), len(matrix[0])
        ans = [[0 for _ in range(H)] for _ in range(W)]
        for h in range(H):
            for w in range(W):
                ans[w][h] = matrix[h][w]      
        return ans
