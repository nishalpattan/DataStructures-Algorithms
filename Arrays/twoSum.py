def twoNumberSum(array, targetSum):
	"""
    Time Complexity : O(n)
    Space Complexity : O(n)
    :param array:
    :param targetSum:
    :return:[number1, number2]
    """
	hash_map = dict()
	for num in array:
		if num in hash_map:
			return [num, targetSum - num]
		hash_map[targetSum - num] = num
	return []

def twoNumberSumSortedArray(array, targetSum):
	"""
	Time Complexity : O(n)
	Space Complexity : O(1)
	:param array:
	:param targetSum:
	:return: [index1, index2]

	Use two pointer method to traverse in a sorted array(non-decreasing),
	if the sum of numbers at start and end index equals target sum, return those indexes
	else if the sum is less than target sum, increment start index , following the increasing order of sorted array
	else if the sum is greater than target sum, decrement end index.
	"""
	start = 0
	end = len(array)-1
	while start <= end:
		curr_sum = array[start]
		if curr_sum == targetSum:
			return[]


if __name__ == "__main__":
    print(twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10))