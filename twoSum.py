def twoNumberSum(array, targetSum):
    # Write your code here.
    # TC : O(n), SC : O(1)
	hash_map = dict()
	for num in array:
		if num in hash_map:
			return [num, targetSum - num]
		hash_map[targetSum - num] = num
	return []

if __name__ == "__main__":
    print(twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10))