class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS = len(board)
        COLS = len(board[0])
        visited = set()
        def dfs(i, j):
            if i >= ROWS or j >= COLS or min(i, j) < 0 or board[i][j] == "X" or (i, j) in visited:
                return
            else:
                board[i][j] = "T"
                visited.add((i, j))
                dfs(i + 1, j)
                dfs(i - 1, j)
                dfs(i, j + 1)
                dfs(i, j - 1)

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == "O" and (i == 0 or j == 0 or i == ROWS - 1 or j == COLS - 1):
                    dfs(i, j)
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == "O":
                    board[i][j] = "X"
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == "T":
                    board[i][j] = "O"