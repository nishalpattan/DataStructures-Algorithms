def solution(input):
    hash_set = set(input)
    output = list()
    for word in input:  # rockstar
        new_word = ""  # ""
        temp_output = list()  # ["rock","star"]
        for letter in word:  # star
            new_word += letter  # start
            if new_word in hash_set and new_word != word:
                print(new_word, word)
                temp_output.append(new_word)
                new_word = ""
        hash_set.remove(word)
        if temp_output != []:
            output.append(temp_output)
    return output



print(solution(["rockstar", "rock", "star", "rocks", "tar", "stars", "rockstars", "super", "highway", "high", "way",
                "superhighway"]))

