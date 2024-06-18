class Solution:
    def check(self, r, c, rlimit, climit):
        return 0 <= r < rlimit and 0 <= c < climit
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        startnum = image[sr][sc]
        image[sr][sc] = newColor
        q = []
        visit = []
        q.append((sr, sc))
        visit.append((sr, sc))
        dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]
        while q:
            qr, qc = q.pop()
            for dir in range(4):
                nr = qr + dr[dir]
                nc = qc + dc[dir]
                if (nr, nc) not in visit and self.check(nr, nc, len(image), len(image[0])):
                    if image[nr][nc] == startnum:
                        visit.append((nr, nc))
                        q.append((nr, nc))
                        image[nr][nc] = newColor                
        return (image)
