class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        fresh = 0
        time = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh+=1
                if grid[r][c] == 2:
                    q.append((r, c))
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while fresh > 0 and q:
            time+=1
            length = len(q)
            """
            we do this because q will change dynamically
            """
            for i in range(length):
                r, c = q.popleft()

                for direction in directions:
                    row, col = r + direction[0], c + direction[1]
                    if row in range(len(grid)) and col in range(len(grid[0])) and grid[row][col] == 1:
                        fresh-=1
                        grid[row][col] = 2
                        q.append((row, col))
        return time if fresh == 0 else -1