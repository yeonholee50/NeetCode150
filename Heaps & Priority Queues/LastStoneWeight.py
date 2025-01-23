class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        q = [-stones[i] for i in range(len(stones))]
        heapq.heapify(q)

        while len(q) > 1:
            stone1 = -heapq.heappop(q)
            stone2 = -heapq.heappop(q)
            res = abs(stone1 - stone2)
            if res != 0:
                heapq.heappush(q, -res)

        return -q[0] if len(q) == 1 else 0