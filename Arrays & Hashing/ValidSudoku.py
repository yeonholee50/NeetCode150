class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        columns = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for i in range(len(board)):
            row = board[i]
            for j in range(len(row)):
                cell = row[j]
                if cell == ".":
                    continue
                if cell in rows[i] or cell in columns[j] or cell in squares[(i//3, j//3)]:
                    return False
                rows[i].add(cell)
                columns[j].add(cell)
                squares[(i//3, j//3)].add(cell)
        return True