class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def manhattan_from_center(point):
            x, y = point
            return math.sqrt((x*x)+(y*y))
        arr = []
        for point in points:
            heapq.heappush(arr, (manhattan_from_center(point), point))

        res = []
        for i in range(k):
            res.append(heapq.heappop(arr)[-1])
        return res
        