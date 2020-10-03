"""
Merge Sort

TC : O(n * logn)

"""
def merge_sort(arr, start, end):
    if end-start +1 <= 1:
        return
    mid = start + (end - start) //2
    merge_sort(arr, start, mid)
    merge_sort(arr, mid+1, end)
    merge(arr, start, mid, end)


def merge(arr, start, mid, end):
    l = start
    r = mid + 1
    temp = list()
    while l <= mid  and r <= end:
        if arr[l] < arr[r]:
            temp.append(arr[l])
            l += 1
        else:
            temp.append(arr[r])
            r += 1
    while l <= mid:
        temp.append(arr[l])
        l += 1
    while r <= end:
        temp.append(arr[r])
        r += 1
    arr[start : end+1] = temp
    # for idx in range(start, end+1):
    #     arr[idx] = temp[idx - start]

if __name__ == "__main__":
    inp_array_1 = [5,6,7,8,1,2,3,4]
    merge_sort(inp_array_1, 0, len(inp_array_1) - 1)
    print(inp_array_1)

    inp_array_2 = [float("inf"), float("-inf"), 0, 3, -3, 5, 6, 7, 8, 1, 2, 2, -4]
    merge_sort(inp_array_2, 0, len(inp_array_2) - 1)
    print(inp_array_2)

