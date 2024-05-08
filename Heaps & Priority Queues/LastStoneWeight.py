class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stone_list = []
        for stone in stones:
            stone_list.append(-stone)
        heapq.heapify(stone_list)

        while len(stone_list) > 1:
            stone1 = -heapq.heappop(stone_list)
            stone2 = -heapq.heappop(stone_list)
            if stone1 != stone2:
                heapq.heappush(stone_list, -abs(stone1-stone2))
        return -stone_list[0] if len(stone_list) != 0 else 0