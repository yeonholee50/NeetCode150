class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)
        ans = None
        for i in range(k):
            ans = heapq.heappop(max_heap)
        return -ans