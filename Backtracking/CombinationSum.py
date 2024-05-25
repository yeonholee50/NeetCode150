class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, combination, total):
            if total == target:
                res.append(combination.copy())
                return
            elif i >= len(candidates) or total > target:
                return
            combination.append(candidates[i])
            dfs(i, combination, total + candidates[i])
            combination.pop()
            dfs(i+1, combination, total)
        dfs(0, [], 0)
        return res