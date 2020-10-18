class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        """
        https://leetcode.com/problems/compare-version-numbers/
        TC : O(n1 + n2)
        SC : O(n1 + n2)
        n1 --> length of version1
        n2 --> lenght of version2
        """
        v1 = version1.split(".")
        v2 = version2.split(".")
        diff = abs(len(v1) - len(v2))
        if diff > 0:
            if len(v1) > len(v2):
                v2 += [0] * diff
            else:
                v1 += [0] * diff
        for idx in range(len(v1)):
            if int(v1[idx]) < int(v2[idx]):
                return -1
            elif int(v1[idx]) > int(v2[idx]):
                return 1
            else:
                continue
        return 0