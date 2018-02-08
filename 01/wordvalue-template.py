from data import DICTIONARY, LETTER_SCORES


def load_words():
    """Load dictionary into a list and return list"""
    mylist = []
    with open(DICTIONARY, 'r') as file:
        for line in file.readlines():
            mylist.append(line.replace('\n', ''))

    return mylist


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    score = 0
    for char in word:
        if char.isalpha():
            score += LETTER_SCORES[char.upper()]

    return score


def max_word_value(words=load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""

    return max(words, key=calc_word_value)


if __name__ == "__main__":
    pass  # run unittests to validate
