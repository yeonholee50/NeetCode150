class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        to get k closest points we need a heapq. we can do a list of tuple with
        (dist, point) like this. heapq automatically will give shortest distance. we can 
        check also if k is greater than or equal to number of points since 
        answer can be in any order. once we check if len points is greater than k, we
         can ignore if k is greater and just do heappop
        """
        if len(points) <= k:
            return points
        def euclid_from_center(point):
            x, y = point
            return math.sqrt(x*x + y*y)
        dist_point = [(euclid_from_center(point), point) for point in points]
        heapq.heapify(dist_point)
        res = []
        for i in range(k):
            res.append(heapq.heappop(dist_point)[-1])
        return res