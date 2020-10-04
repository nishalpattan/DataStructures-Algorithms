def binary_search(input_array, value):
    length = len(input_array)
    if length == 0:
        return "Not Found"
    elif length == 1 and value == input_array[0]:
        return "Found"
    elif length ==1 and value > input_array[0]:
        return "Not Found"
    else:
        l1 = input_array[0:length//2]
        l2 = input_array[length//2:length]
        if len(l2) > 0 and value >= l2[0]:
            return binary_search(l2, value)
        else:
            return binary_search(l1, value)


if __name__ == "__main__":
    print(binary_search([1, 2, 3,4,6], 10))
    print(binary_search([-1,0,3,5,9,12], 9))
    print(binary_search([1, 2, 3,4,6], 10))
