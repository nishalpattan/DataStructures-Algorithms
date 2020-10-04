"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal


class TestFinder(object):

    def test(self, sol):
        assert_equal(sol([5, 5, 7, 7], [5, 7, 7]), 5)
        assert_equal(sol([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6]), 5)
        assert_equal(sol([9, 8, 7, 6, 5, 4, 3, 2, 1], [9, 8, 7, 5, 4, 3, 2, 1]), 6)
        assert_equal(sol([9, 8, 7, 6, 5, 4, 3, 2, 1], [9, 8, 7, 6,5, 4, 3, 2, 1]), None)
        print('ALL TEST CASES PASSED')


def finder(arr1, arr2):
    hashTable = dict()
    for i in arr1:
        if i in hashTable:
            hashTable[i] += 1
        else:
            hashTable[i] = 1
    for j in arr2:
        if j in hashTable:
            hashTable[j] -= 1
    for k in hashTable.keys():
        if hashTable[k] != 0:
            return k
    return None

# Run test
t = TestFinder()
t.test(finder)