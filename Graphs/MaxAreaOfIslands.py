class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        land_set = set()
        max_area = 0
        current_area = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        def dfs(i, j):
            nonlocal current_area
            if min(i, j) < 0 or i >= ROWS or j >= COLS or grid[i][j] == 0 or (i, j) in land_set:
                return
            else:
                land_set.add((i, j))
                current_area+=1
                dfs(i, j + 1)
                dfs(i, j - 1)
                dfs(i + 1, j)
                dfs(i - 1, j)


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in land_set:
                    current_area = 0
                    dfs(i, j)
                    max_area = max(max_area, current_area)
        return max_area
        