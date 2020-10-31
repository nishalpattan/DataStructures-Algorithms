class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        https://leetcode.com/problems/group-anagrams/
        https://leetcode.com/problems/group-anagrams/
        TC : O(N * K)
        SC : O(N * K)
        N --> length of strs
        K --> length of single str
        """
        hash_map = dict()
        for _str in strs:
            char_count = [0] * 26
            for char in _str:
                char_count[ord(char) - ord('a')] += 1
            if tuple(char_count) in hash_map:
                hash_map[tuple(char_count)].append(_str)
            else:
                hash_map[tuple(char_count)] = [_str]
        return hash_map.values()

        """
        https://leetcode.com/problems/group-anagrams/
        TC : O(N * K * logK)
        SC : O(N * K)
        N --> length of strs
        K --> length of single str
        """
        hash_map = dict()
        for _str in strs:
            sorted_str = "".join(sorted(_str))
            if sorted_str in hash_map:
                hash_map[sorted_str].append(_str)
            else:
                hash_map[sorted_str] = [_str]
        return hash_map.values()

