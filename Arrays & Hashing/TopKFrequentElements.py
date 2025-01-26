class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        for num in nums:
            if num in hm.keys():
                hm[num]+=1
            else:
                hm[num] = 1

        q = []
        for num in hm.keys():
            heapq.heappush(q, (-hm[num], num))
        
        if len(q) <= k:
            return list(hm.keys())
        else:
            res = []
            for _ in range(k):
                res.append(heapq.heappop(q)[-1])
            return res 