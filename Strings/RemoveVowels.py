def remove_vowels(chars):
    """
    https://leetcode.com/problems/remove-vowels-from-a-string

    :param chars: string
    :return: string without vowels
    """
    stack = list()
    vowel_set = {"a","e","i","o","u"}
    for char in chars:
        if char.lower() not in vowel_set:
            stack.append(char)
    return "".join(stack)

if __name__ == "__main__":
    assert(remove_vowels("nishal") == "nshl")
    assert(remove_vowels("abc") == "bc")
    assert (remove_vowels("aeiou") == "")
    assert (remove_vowels("byte") == "byt")
    assert (remove_vowels("xyz") == "xyz")