def fact(num):
    if num == 0:
        return 1
    else:
        return num * fact(num-1)

if __name__ == "__main__":
    print(fact(5))
    print(fact(1))
    print(fact(0))
