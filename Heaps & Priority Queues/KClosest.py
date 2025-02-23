class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def euclid(point):
            x, y = point[0], point[1]

            return math.sqrt(x**2 + y**2)
        q = []
        for point in points:
            heapq.heappush(q, (-euclid(point), point))
            if len(q) > k:
                heapq.heappop(q)
        return [q[i][1] for i in range(len(q))]