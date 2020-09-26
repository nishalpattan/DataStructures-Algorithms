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
