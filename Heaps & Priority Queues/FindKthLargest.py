class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        kth largest q. If list is too big, we can just do -
        """
        ls = [-num for num in nums]
        heapq.heapify(ls)
        res = None
        for i in range(k):
            res = -heapq.heappop(ls)
        return res