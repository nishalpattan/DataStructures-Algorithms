def mul(num1,num2):
    if num2 == 0:
        return 0;
    else:
        if num2 > num1: num1,num2 = num2,num1
        Sum = num1 + mul(num1, num2 - 1)
        return Sum

if __name__ == "__main__":
    print(mul(2,3))
    print(mul(10,20))