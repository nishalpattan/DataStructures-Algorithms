def issubstring(s1,s2):
    stack = list(s2)
    popped_element = ""
    while(stack):
        popped_element = stack.pop() + popped_element
        s2 =  popped_element + "".join(stack)
        if s2 == s1:
            return True
    return False


def string_rotation(s1,s2):
    return issubstring(s1,s2)


if __name__ == "__main__":
    print(string_rotation("waterbottle","erbottlewat"))
    print(string_rotation("abcde","cdeab"))
    print(string_rotation("abcde","abced"))