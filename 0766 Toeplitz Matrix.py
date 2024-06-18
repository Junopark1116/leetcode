class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        H, W = len(matrix), len(matrix[0])      
        for w in range(W-1):
            for h in range(H-1):
                if matrix[h][w] != matrix[h+1][w+1]:
                    return False  
        return True
