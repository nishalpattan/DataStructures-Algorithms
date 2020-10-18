class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        https://leetcode.com/problems/longest-substring-without-repeating-characters/
        TC : O(n)
        SC : O(n)
        """
        if s is None or len(s) == 0:
            return 0
        long_str = [0,1]
        start_idx = 0
        hash_map = dict()
        for idx, char in enumerate(s):
            if char in hash_map:
                start_idx = max(start_idx, hash_map[char] + 1)
            if idx + 1 - start_idx > long_str[1] - long_str[0]:
                long_str[0] = start_idx
                long_str[1] = idx + 1
            hash_map[char] = idx
        return long_str[1] - long_str[0]