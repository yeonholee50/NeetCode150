class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        simple question, just a tuple with euclid dist and points 
        and a simple heapq call
        """
        dist = []
        for point in points:
            x, y = point
            heapq.heappush(dist, (math.sqrt((x * x) + (y * y)), point))
        res = []
        for i in range(k):
            _, point = heapq.heappop(dist)
            res.append(point)
        return res