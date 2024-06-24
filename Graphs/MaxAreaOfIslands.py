class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        island_locations = set()
        max_area = 0
        count = 0
        def dfs(i, j):
            nonlocal count
            nonlocal max_area
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or (i, j) in island_locations or grid[i][j] == 0:
                return
            else:
                count+=1
                island_locations.add((i, j))
                dfs(i, j + 1)
                dfs(i, j - 1)
                dfs(i + 1, j)
                dfs(i - 1, j)
                max_area = max(max_area, count)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                count = 0
                if grid[i][j] == 1 and (i, j) not in island_locations:
                    dfs(i, j)
        return max_area
        