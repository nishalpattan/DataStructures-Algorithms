def subarraySort(array):
    # Write your code here.
    min_num = float("inf")
    max_num = float("-inf")
    indices = [-1,-1]
    for idx in range(len(array)):
        if idx == 0:
            if not(array[idx] <= array[idx+1]):
                min_num = min(min_num, array[idx])
                max_num = max(max_num, array[idx])
        elif idx == len(array) - 1:
            if not(array[idx-1] <= array[idx]):
                min_num = min(min_num, array[idx])
                max_num = max(max_num, array[idx])
        elif not(array[idx-1] <= array[idx] <= array[idx+1]):
            min_num = min(min_num, array[idx])
            max_num = max(max_num, array[idx])
    if min_num == float("inf") or max_num == float("-inf"):
        return [-1, -1]
    for idx in range(len(array)):
        if min_num < array[idx]:
            indices[0] = idx
            break
    for idx in range(len(array)-1, -1, -1):
        if max_num > array[idx]:
            indices[-1] = idx
            break
    return indices

if __name__ == "__main__":
    print(subarraySort([1,2,4,3,7,6]))