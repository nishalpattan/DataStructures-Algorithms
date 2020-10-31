class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        https://leetcode.com/problems/missing-number/submissions/
        Approach using Set
        TC : O(n)
        SC : O(n)
        """
        hash_set = set()
        for num in nums:
            hash_set.add(num)

        for idx in range(len(nums) + 1):
            if idx not in hash_set:
                return idx

        """
        https://leetcode.com/problems/missing-number/submissions/
        TC : O(n)
        SC : O(1)
        """
        n = len(nums)
        input_sum = 0
        range_sum = 0
        for num in nums:
            input_sum += num

        for num in range(0, n + 1):
            range_sum += num

        return abs(range_sum - input_sum)
