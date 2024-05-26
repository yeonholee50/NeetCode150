class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        points = set()
        for x, y, r in circles:
            points.add((x, y))
            points.add((x + r, y))
            points.add((x - r, y))
            points.add((x, y + r))
            points.add((x, y - r))
            for i in range(x-r+1, x+r):
                for j in range(y-r+1, y+r):
                    if (i,j) not in points and (i - x) ** 2 + (j - y) ** 2 <= r ** 2:
                        points.add((i,j))
        return len(points)