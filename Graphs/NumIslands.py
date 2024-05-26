class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        visit = set()
        islands = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(i, j):
            if i not in range(rows) or j not in range(cols) or grid and grid[i][j] == "0" or (i, j) in visit:
                return
            else:
                visit.add((i, j))
                directions = [[-1,0], [1, 0], [0, -1], [0, 1]]
                for direction in directions:
                    dfs(direction[0] + i, direction[1] + j)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i, j) not in visit:
                    dfs(i, j)
                    islands+=1
        return islands
