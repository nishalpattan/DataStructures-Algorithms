def string_compress(input_string):
    new_string = []
    count = 1
    for i in range(len(input_string)):
        if input_string[i] not in new_string:
            new_string.append(input_string[i])
        if i+1 != len(input_string) and input_string[i] == input_string[i+1]:
            count = count + 1
        else:
            new_string.append(str(count))
            count = 1
    return "".join(new_string)

if __name__ == "__main__":
    print(string_compress("AAABCCDDDDD"))
    print(string_compress("AAB"))