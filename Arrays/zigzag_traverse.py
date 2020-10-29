def zigzagTraverse(array):
    # Write your code here.
    row = 0
    col = 0
    going_down = True
    result = list()
    while not(row < 0 or col < 0 or row > len(array)-1 or col > len(array[0]) - 1):
        result.append(array[row][col])
        if going_down:
            if col == 0 or row == len(array) - 1:
                going_down = False
                if row == len(array) - 1:
                    col += 1
                else:
                    row += 1
            else:
                row += 1
                col -= 1
        else:
            if row == 0 or col == len(array[0]) - 1:
                going_down = True
                if col == len(array[0])-1:
                    row += 1
                else:
                    col += 1
            else:
                row -= 1
                col += 1
    return result

if __name__ == "__main__":
    print(zigzagTraverse([[1, 3, 4, 10], [2, 5, 9, 11], [6, 8, 12, 15], [7, 13, 14, 16]]))