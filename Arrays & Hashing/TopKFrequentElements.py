class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elements_freq = {}
        for num in nums:
            if num not in elements_freq.keys():
                elements_freq[num] = -1
            else:
                elements_freq[num]-=1
        keys = elements_freq.keys()
        heap = []
        for key in keys:
            heapq.heappush(heap, (elements_freq[key], key))
        res = []
        while k != 0:
            res.append(heapq.heappop(heap)[-1])
            k-=1
        return res