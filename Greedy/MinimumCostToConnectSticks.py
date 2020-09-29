import heapq
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        """
        https://leetcode.com/problems/minimum-cost-to-connect-sticks/submissions/

        using Heap, Greedy Approach
        TC : O(n)
        SC : O(n)

        """
        cost = 0
        min_heap = list()
        for stick in sticks:
            heapq.heappush(min_heap, stick)
        while len(min_heap) > 1:
            curr_cost = heapq.heappop(min_heap) + heapq.heappop(min_heap)
            cost += curr_cost
            heapq.heappush(min_heap, curr_cost)
        return cost