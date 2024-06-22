class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(arr, i, summation):
            if summation == target:
                res.append(arr.copy())
                return
            if i >= len(candidates) or summation > target:
                return
            arr.append(candidates[i])
            dfs(arr, i, summation + candidates[i])
            arr.pop()
            dfs(arr, i + 1, summation)
                
        dfs([], 0, 0)
        return res