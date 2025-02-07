class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = None
        if target <= matrix[0][-1]:
            """
            search first row
            """
            row = matrix[0]

        else:
            i = 1
            while i < len(matrix) and matrix[i][-1] < target:
                i*=2
            if i >= len(matrix):
                i = len(matrix) - 1
            while i > 0 and matrix[i][0] > target:
                i-=1
            if i <= 0:
                return False
            row = matrix[i]
            print(row)
        if row[0] >= target:
            return True if target == row[0] else False
        i = 1
        while i < len(row) and row[i] < target:
            i*=2
        if i >= len(row):
            i = len(row) - 1
        while i > 0 and row[i] > target:
            i-=1
        if i <= 0:
            return False
        else:
            return row[i] == target