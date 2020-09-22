class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        https://leetcode.com/problems/longest-increasing-subsequence/submissions/
        Dynamic Programming Approach
        n --> length on input nums list
        TC : O(n ^ 2)
        SC : O(n)
        """
        if nums is None or len(nums) == 0:
            return 0
        LIS = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    LIS[i] = max(LIS[i], LIS[j] + 1)
        print(LIS)
        return max(LIS)