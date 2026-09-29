class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        #directions = [(-1,0), (1, 0), (0,-1), (0,1)]

        mx_area = 0

        def dfs(r,c):
            if r < 0 or r > len(grid)-1:
                return 0
            if c < 0 or c > len(grid[0])-1:
                return 0
            
            if grid[r][c] == 0:
                return 0
            if (r,c) in visited:
                return 0
            count = 1
            visited.add((r,c))
            return count + (dfs(r-1, c)+ dfs(r+1,c) + dfs(r,c-1)+dfs(r, c+1))
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and (r, c) not in visited:
                    curr = dfs(r,c)
                    mx_area = max(mx_area, curr)
        return mx_area
        