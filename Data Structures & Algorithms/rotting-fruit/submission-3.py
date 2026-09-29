from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        minutes = 0
        fresh = 0
        visited = set()
        # calculate num of fresh fruit and add rotten fruit
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh +=1
                elif grid[r][c] == 2:
                    q.append((r, c))
        # run bfs
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr = dr + r
                    nc = dc + c
                    if 0<= nr < ROWS and 0<= nc < COLS:
                        if grid[nr][nc] == 1:
                            grid[nr][nc] = 2
                            fresh-=1
                            q.append((nr, nc))
                            # visited.append(nr,nc)
            minutes +=1
        return minutes if fresh == 0 else -1
            
        