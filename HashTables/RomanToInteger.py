class Solution:
    def romanToInt(self, s: str) -> int:
        """
        https://leetcode.com/problems/roman-to-integer/
        TC : O(n)
        SC : O(1)
        """
        hash_map = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        num = 0
        for idx in range(len(s) - 1):
            if hash_map[s[idx]] < hash_map[s[idx+1]]:
                num -= hash_map[s[idx]]
            else:
                num += hash_map[s[idx]]
        num += hash_map[s[-1]]
        return num