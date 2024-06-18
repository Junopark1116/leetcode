class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        sqr = 0 
        cl = 0  
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    sqr += 1
                    if i == 0 and j > 0 and grid[0][j-1] == 1:
                        cl += 1
                    elif j == 0 and i > 0 and grid[i-1][0] == 1:
                        cl += 1
                    elif i != 0 and j != 0:
                        if grid[i-1][j] == 1: cl += 1
                        if grid[i][j-1] == 1: cl += 1
        return (sqr*4) - (cl*2)
