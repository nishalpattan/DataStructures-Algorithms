def reverseArray(a):
    i = len(a) - 1
    j = 0
    while j < i:
        print(j,i)
        a[j],a[i] = a[i],a[j]
        j = j+1
        i = i-1
        print(a)
    return a

if __name__ == "__main__":
    print(reverseArray([1,2,3]))