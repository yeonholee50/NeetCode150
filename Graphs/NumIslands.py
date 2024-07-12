class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        nums = 0
        land = set()
        def dfs(i, j):
            if min(i, j) < 0 or i >= ROWS or j >= COLS or grid[i][j] == "0" or (i, j) in land:
                return
            else:
                land.add((i, j))
                dfs(i + 1, j)
                dfs(i - 1, j)
                dfs(i, j + 1)
                dfs(i, j - 1)


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i, j) not in land:
                    nums+=1
                    dfs(i, j)
        return nums