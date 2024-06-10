class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(curr, position, target):
            if target == 0:
                res.append(curr.copy())
                return
            elif target <= 0:
                return
            previous = None
            for i in range(position, len(candidates)):
                if previous == candidates[i]:
                    continue
                else:
                    curr.append(candidates[i])
                    backtrack(curr, i + 1, target - candidates[i])
                    curr.pop()
                    previous = candidates[i]
        
        backtrack([], 0, target)
        return res