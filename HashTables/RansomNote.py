"""
https://leetcode.com/problems/ransom-note/
TC : O(n)
SC : O(n)
"""
def ransom_note(paragraph, text):
    hash_map = dict()
    for char in text:
        hash_map[char] = hash_map.get(char, 0) + 1

    for char in paragraph:
        if hash_map.get(char, 0) == 0:
            return False
        hash_map[char] -= 1
    return True

if __name__ == "__main__":
    assert ransom_note("cat", "bat") == False
    assert ransom_note("dog", "didnotgo") == True