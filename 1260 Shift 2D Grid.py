class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        H, W = len(grid), len(grid[0])
        ngrid = [[0 for _ in range(W)] for _ in range(H)]
        k %= (H*W)
        for h in range(H):
            for w in range(W):
                temp = h*W + w + k
                dh, dw = temp//W, temp%W
                ngrid[dh%H][dw%W] = grid[h][w]
        return ngrid
