"""
Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?
"""

def isUnique(Str):
    """
    :param Str:
    :return: bool
    Time Complexity : O(N)
    Space Complexity : O(N)
    """
    hashSet = set()
    for char in Str:
        if char in hashSet:
            return False
        hashSet.add(char)
    return True

def isUnique_NoAddition_DataStructure(Str):
    """
    Time Complexity: O(NlogN)
    Space Complexity : O(1)
    :param Str:
    :return: bool
    """
    sortedStr = sorted(Str)
    for idx in range(len(sortedStr) - 1):
        if sortedStr[idx] == sortedStr[idx+1]:
            return False
    return True

if __name__ == "__main__":
    s1 = "nishal"
    s2 = "nishaaal"
    print(isUnique(s1))
    print(isUnique_NoAddition_DataStructure(s1))
    print(isUnique(s2))
    print(isUnique_NoAddition_DataStructure(s2))