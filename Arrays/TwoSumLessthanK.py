def twoSumLessThanK(nums, k):
    """
    Given an array nums of integers and integer k,
    return the maximum sum such that there exists i < j,
     with nums[i] + nums[j] = sum and sum < k.
    If no i, j exist satisfying this equation, return -1

    :param nums:
    :param k:
    :return: max sum
    Time Complexity : O(n * logn)
    Space Complexity : O(1)
    """
    nums.sort()
    start = 0
    end = len(nums) - 1
    max_sum = -1
    while start < end:
        curr_sum = nums[start] + nums[end]
        if curr_sum < k:
            max_sum = max(curr_sum, max_sum)
        if curr_sum >= k:
            end -= 1
        else:
            start += 1

    return max_sum