class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        brute force would be to take every gas station and go around until you hit back to your starting position
        There's only one answer so if O(n^2) this could take a long time
        """
        if sum(gas) < sum(cost):
            return -1
        """
        there's a solution
        """
        total, res = 0, 0
        for i in range(len(gas)):
            total+=(gas[i] - cost[i])
            if total < 0:
                total = 0
                res = i + 1
        return res