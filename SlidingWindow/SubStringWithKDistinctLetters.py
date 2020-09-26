"""
https://leetcode.com/discuss/interview-question/370112

Problem similar to Longest SubString without Repeating Characters

TC : O(n)
SC : O(n)
"""


def substrings_with_k_unique_chars(s, k):
    hash_map = dict()
    start = 0
    res = set()

    for idx, char in enumerate(s):
        if char in hash_map:
            start = max(hash_map[char] + 1, start)
        if idx+1 - start == k:
            res.add(s[start : idx+1])
            start += 1
        hash_map[char] = idx
    return list(res)

if __name__ == "__main__":
    print(substrings_with_k_unique_chars("abcabc", 3))
    print(substrings_with_k_unique_chars("aa", 1))
    print(substrings_with_k_unique_chars("awaglknagawunagwkwagl", 4))

