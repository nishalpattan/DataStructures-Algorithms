def groupAnagrams(words):
    # Write your code here.
    hash_map = dict()
    for word in words:
        sorted_word = "".join(sorted(word))
        if sorted_word in hash_map:
            hash_map[sorted_word].append(word)
        else:
            hash_map[sorted_word] = [word]
    return list(hash_map.values())

if __name__ == "__main__":
    print(groupAnagrams(["yo","act","flop","tac","cat","oy","olfp"]))
