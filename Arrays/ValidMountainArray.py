def validMountainArray(A):
    if len(A) < 3:
        return False
    max_num = max(A)
    index_of_max = A.index(max_num)
    increase = True
    decrease = True
    for i in range(1, index_of_max+1):
        if A[i] < A[i-1]:
            increase = False
    for j in range(index_of_max, len(A)):
        if A[j] == A[j-1] and j+1 == len(A):
            return  False
        if A[j] > A[j - 1]:
            print(j, A[j],A[j-1])
            decrease = False
    return increase and decrease

if __name__ == "__main__":
    print(validMountainArray([3,5,5]))
    print(validMountainArray([0,3, 2, 1]))