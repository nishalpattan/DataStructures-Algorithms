numberMap = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def Sum(num1, num2):
    print(num1)
    num = toInteger(num1) + toInteger(num2)
    print(num)
    return str(num)


def toInteger(input_num):
    number = 0
    increment = 1
    for i in range(-1, -(len(input_num) + 1), -1):
        print(input_num[i])
        if input_num[i] in numberMap:
            number = number + (increment * numberMap[input_num[i]])
            increment = increment * 10
    return number