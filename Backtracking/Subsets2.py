class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        we can do an in search but that takes too long. why not add
        and for the second part skip through all that are equal
        """
        nums.sort()
        res = []
        subset = []
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i+=1
            dfs(i + 1)
        dfs(0)
        return res 