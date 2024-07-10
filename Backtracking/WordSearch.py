class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(i, r, c):
            if i >= len(word):
                return True
            elif min(r, c) < 0 or r >= ROWS or c >= COLS or board[r][c] != word[i] or (r, c) in path:
                return False
            path.add((r, c))
            exists = dfs(i + 1, r + 1, c) or dfs(i + 1, r - 1, c) or dfs(i + 1, r, c + 1) or dfs(i + 1, r, c - 1)
            path.remove((r, c))
            return exists
        for i in range(len(board)):
            for j in range(len(board[i])):
                if dfs(0, i, j):
                    return True
        return False
