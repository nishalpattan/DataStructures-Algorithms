"""
https://leetcode.com/problems/decompress-run-length-encoded-list/
TC : O(n)
SC : O(n)
"""
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res = list()
        for i in range(1, len(nums),2):
            res += [nums[i]] * nums[i-1]
        return res