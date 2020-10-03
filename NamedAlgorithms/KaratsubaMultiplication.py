def karatsuba_multiplication(num1, num2):
    if int(num1) < 10 or int(num2) < 10:
        return int(num1) * int(num2)
    m = max(len(num1), len(num2))
    m2 = m // 2

    a = int(num1) // 10 ** m2
    b = int(num1) % 10 ** m2
    c = int(num2) // 10 ** m2
    d = int(num2) % 10 ** m2



    z0 = karatsuba_multiplication(str(b), str(d))
    z1 = karatsuba_multiplication(str(int(b) + int(a)), str(int(c) + int(d)))
    z2 = karatsuba_multiplication(str(a), str(c))

    return (z2 * 10 ** (m2 * 2)) + ((z1 - z2 - z0) * 10 ** m2) + z0

if __name__ == "__main__":
    num1 = "1234"
    num2 = "5678"
    print(karatsuba_multiplication(num1, num2))

    num_1 = "3141592653589793238462643383279502884197169399375105820974944592"
    num_2 = "2718281828459045235360287471352662497757247093699959574966967627"

    # Coursera Stanford assignment

    print(karatsuba_multiplication(num_1, num_2))