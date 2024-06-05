class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def euclid_distance_from_origin(point):
            x, y = point
            return math.sqrt(x*x + y*y)
        q = []
        for point in points:
            heapq.heappush(q, (euclid_distance_from_origin(point), point))
        res = []
        for i in range(k):
            res.append(heapq.heappop(q)[-1])
        return res