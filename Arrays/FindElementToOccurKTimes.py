from collections import OrderedDict
def findKTimes(nums,k):
    hashTable = OrderedDict()
    for i in nums:
        if i in hashTable:
            hashTable[i] += 1
        else:
            hashTable[i] = 1
    for j in nums:
        if hashTable[j] == k:
            return j
    return -1


if __name__ == '__main__':
    print(findKTimes([1, 7, 4, 3, 4, 8, 7],2))
    print(findKTimes([4, 1, 6, 1, 6, 4], 1))