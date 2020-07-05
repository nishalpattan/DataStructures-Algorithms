def checkIfDoubleExist(arr):
    print(binarySearch(sorted(arr),0,len(arr)))

def binarySearch( nums, low, high):
    if low > high: return -1
    mid = low + (high - low) // 2
    target = nums[mid] * 2
    if mid != len(nums) and target in nums:
        return True
    else:
        return binarySearch(nums,mid+1, high)
    return False