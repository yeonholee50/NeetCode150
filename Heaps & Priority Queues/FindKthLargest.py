class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr = [-num for num in nums]
        heapq.heapify(arr)
        res = None
        for i in range(k):
            res = -heapq.heappop(arr)
        return res