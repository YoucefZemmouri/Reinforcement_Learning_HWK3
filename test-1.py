sentence = ' Hi my  name is zemmouri Youcef  '


def inverse_word(word):
    inversed_word = []
    n = len(word)
    for i in range(n - 1, -1, -1):
        inversed_word.append(word[i])
    return inversed_word


def inverse_sentence(sentence):
    inversed_sentence = []
    space_begin = 0
    space_end = 0

    while (space_begin < len(sentence) and space_end < len(sentence)):
        while sentence[space_begin] != ' ' and space_begin < len(sentence):
            space_begin += 1

        space_end = space_begin + 1
        while sentence[space_end] != ' ' and space_end < len(sentence):
            space_end += 1

        if space_end - space_begin > 0:
            inversed_sentence.append(inverse_word(sentence[space_begin:space_end]))
            space_begin = space_end + 1

    return inversed_sentence


print(sentence)
print(inverse_sentence(sentence))
