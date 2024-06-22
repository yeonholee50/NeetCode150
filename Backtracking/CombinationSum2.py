class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        """
        we can reduce num of recursion by sorting so that i+1 will be greater than previous
        """
        res = []
        def dfs(combination, i, summation):
            if summation == target:
                res.append(combination.copy())
                return
            if summation > target or i >= len(candidates):
                return
            prev = -1
            for j in range(i, len(candidates)):
                if candidates[j] == prev:
                    continue
                combination.append(candidates[j])
                dfs(combination, j + 1, summation + candidates[j])
                combination.pop()
                prev = candidates[j]
        dfs([], 0, 0)
        return res