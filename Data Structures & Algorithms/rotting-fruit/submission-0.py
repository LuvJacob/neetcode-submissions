class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque() # create q
        fresh = 0 # amount of fresh fruits
        time = 0 # time it takes to turn all fruit rotten

        # algorithm to catch all fresh fruit number
        for r in range(len(grid)): # which row r u on
            for c in range(len(grid[0])): # which column are you on
                if grid[r][c] == 1: # if fruit is fresh
                    fresh +=1 # increase fresh fruit
                if grid[r][c]==2:       #append location of rotten to q
                    q.append((r, c))
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        while fresh > 0 and q:
            l = len(q)
            for i in range(l):
                r, c = q.popleft()

                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (row in range(len(grid)) and col in range(len(grid[0])) and grid[row][col] == 1):
                        grid[row][col] = 2
                        q.append((row,col))
                        fresh -=1
            time +=1
        return time if fresh == 0 else -1
                
        