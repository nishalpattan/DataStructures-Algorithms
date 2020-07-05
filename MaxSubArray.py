from nose.tools import assert_equal

"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""


class TestFinder(object):

    def test(self, sol):
        assert_equal(sol([1, 2, 3]), 6)
        assert_equal(sol([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
        print('ALL TEST CASES PASSED')


def max_sub_array(nums):
    curr_sum = 0
    best_sum = 0
    for num in nums:
        curr_sum = max(0,curr_sum + num)
        best_sum = max(best_sum,curr_sum)
    print(best_sum)
    return best_sum




# Run test
t = TestFinder()
t.test(max_sub_array)