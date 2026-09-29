class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        count = 0
        def dfs(r, c):
            if r < 0 or r >= ROWS or c < 0 or c>= COLS:
                return
            if grid[r][c] == "0":
                return
            if (r, c) in visited:
                return
            visited.add((r, c))
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r, c) not in visited:
                    count +=1
                    dfs(r,c)
        return count