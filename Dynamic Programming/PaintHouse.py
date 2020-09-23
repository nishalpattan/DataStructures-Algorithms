class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        """
        https://leetcode.com/problems/paint-house/
        Dynamic Programming Approach
        TC : O(n)
        SC : O(1)
        """
        if costs is None or len(costs) == 0:
            return 0
        n = len(costs)
        for i in range(1, n):
            costs[i][0] += min(costs[i - 1][1], costs[i - 1][2])
            costs[i][1] += min(costs[i - 1][0], costs[i - 1][2])
            costs[i][2] += min(costs[i - 1][0], costs[i - 1][1])
        return min(costs[n - 1][0], costs[n - 1][1], costs[n - 1][2])