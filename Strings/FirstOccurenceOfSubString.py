class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        https://leetcode.com/problems/implement-strstr
        TC : O((n -l) * l)
        SC : O(1)
        n -- > length of haystack
        l --> length of needle
        """
        if len(needle) == 0:
            return 0
        window_size = len(needle)
        for idx in range(len(haystack)):
            if haystack[idx : idx+window_size] == needle:
                return idx
        return -1