class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        """
        list needs to be of size k. the one at the top should bethe kth largest and the one at the end should be the largest
        we should pop the smallest
        """
        self.nums = nums
        self.k = k
        heapq.heapify(self.nums)
        while len(self.nums) > k:
            heapq.heappop(self.nums)



    def add(self, val: int) -> int:
        if len(self.nums) < self.k:
            heapq.heappush(self.nums, val)
            return self.nums[0]
        else:
            if self.nums[0] > val:
                return self.nums[0]
            else:
                heapq.heappop(self.nums)
                heapq.heappush(self.nums, val)
                return self.nums[0]
            return res