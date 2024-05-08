class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        we can do min of 1 or 2 because the 0th depends on the min solution
        we can do this because we can start on either index 0 or index 1
        """
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])

        return min(cost[0], cost[1])