class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        arr = None
        if matrix[0][-1] >= target:
            arr = matrix[0]
        else:
            i = 1
            while i < len(matrix) and matrix[i][-1] < target:
                i*=2
            if i >= len(matrix):
                i = len(matrix) - 1
            while i > 0 and matrix[i][0] > target:
                i-=1
            arr = matrix[i]
        if arr[0] == target:
            return True
        i = 1
        while i < len(arr) and arr[i] < target:
            i*=2
        if i >= len(arr):
            i = len(arr) - 1
        while i > 0 and arr[i] > target:
            i-=1
        return arr[i] == target