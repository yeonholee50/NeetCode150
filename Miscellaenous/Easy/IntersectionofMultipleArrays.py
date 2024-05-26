class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        distinct = set()
        for num in nums[0]:
            distinct.add(num)
        for i in range(1, len(nums)):
            nums[i].sort()
            arr = nums[i]
            check = set()
            for j in range(len(arr)):
                if arr[j] in distinct:
                    check.add(arr[j])
            distinct = check
        res = []
        for num in distinct:
            res.append(num)
        res.sort()
        return res