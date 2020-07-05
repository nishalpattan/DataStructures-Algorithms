import sys
def findPeak(nums):
    mid = len(nums) // 2
    if(nums[mid] < nums[mid - 1]):
        return findPeak(nums[:mid + 1])
    elif(nums[mid] < nums[mid + 1]):
        return findPeak(nums[mid+1:])
    else:
        return nums[mid]

def main():
    numsList = [2,3,1,4]
    print(findPeak(numsList))

if __name__ == '__main__':{
    main()
}
