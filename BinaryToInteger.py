def binaryTointeger(num):
    exponent = 0
    totalSum = 0
    while num // 10 != 0:
        totalSum = totalSum + (2 ** exponent) * (num % 10)
        num = num // 10
        exponent = exponent + 1
    totalSum = totalSum + (2 ** exponent) * (num % 10)
    return totalSum

def integerToBinary(num):
    stack = []
    while num // 2 != 0:
        stack.append(str(num % 2))
        num = num // 2
    stack.append(str(num))
    return "".join(stack[::-1])

if __name__ == "__main__":
    print(binaryTointeger(101))
    print(integerToBinary(256))