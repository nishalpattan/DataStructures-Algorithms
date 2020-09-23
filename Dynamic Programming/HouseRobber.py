class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        https://leetcode.com/problems/house-robber/
        Dynamic Programming Approach
        TC : O(n)
        SC : O(n)
        """
        if nums is None or len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
        return dp[len(nums) - 1]