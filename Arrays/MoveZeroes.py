def move_zeroes(arr):
    p1 = 0
    for p2 in range(len(arr)):
        if arr[p2] != 0:
            arr[p1] = arr[p2]
            p1 += 1
    for i in range(p1, len(arr)):
        arr[i] = 0
    return arr

if __name__ == "__main__":
    arr = [3,7,0,5,0,2]
    assert (move_zeroes(arr) == [3,7,5,2,0,0])