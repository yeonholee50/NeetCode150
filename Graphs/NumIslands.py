class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num = 0

        island_locations = set()
        

        def dfs(i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or (i, j) in island_locations or grid[i][j] == "0":
                return
            else:
                island_locations.add((i, j))            
                dfs(i + 1, j)
                dfs(i - 1, j)
                dfs(i, j + 1)
                dfs(i, j - 1)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i, j) not in island_locations:
                    num+=1
                    dfs(i, j)
        return num