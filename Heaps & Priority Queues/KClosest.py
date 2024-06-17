class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if len(points) <= k:
            return points
        def euclid_from_center(point):
            x, y = point
            return math.sqrt(x*x + y*y)
        arr = [(euclid_from_center(point), point) for point in points]
        heapq.heapify(arr)
        res = []
        for i in range(k):
            res.append(heapq.heappop(arr)[-1])
        return res