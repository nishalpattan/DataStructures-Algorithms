"""
Check if s1 is sub sequence of s2
https://leetcode.com/problems/is-subsequence/
TC : O(n)
SC : O(1)
"""

def is_sub_sequence(s1, s2):
    if len(s1) == 0:
        return True
    if len(s2) == 0:
        return False
    idx = 0
    for char in s2:
        if char == s1[idx]: idx += 1
        if idx == len(s1):
            return True
    return False

"""
Check if s1 is sub sequence of s2
https://leetcode.com/problems/is-subsequence/
Approach using Stack
TC : O(n)
SC : O(n)
"""
def is_sub_sequence_using_stack(s1, s2):
    if len(s1) == 0:
        return True
    if len(s2) == 0:
        return False
    stack = list()
    idx = 0
    for char in s2:
        stack.append(char)
        if stack[-1] == s1[idx]: idx += 1
        else: stack.pop()
        if len(stack) == len(s1):
            return True
    return len(stack) == len(s1)

if __name__ == "__main__":
    assert (is_sub_sequence("cpu", "computer") == True)
    assert (is_sub_sequence("abc", "aabbcc") == True)
    assert (is_sub_sequence("xyz", "axbyc") == False)
    assert (is_sub_sequence("", "abc") == True)

    # test stack approach
    assert(is_sub_sequence_using_stack("cpu", "computer") == True)
    assert (is_sub_sequence_using_stack("abc", "aabbcc") == True)
    assert (is_sub_sequence_using_stack("xyz", "axbyc") == False)
    assert(is_sub_sequence_using_stack("", "abc") == True)