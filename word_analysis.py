from collections import defaultdict
import json


def load_words(textfile_name):
    ''' Returns: Loaded list of words from txt. '''
    textfile = open(textfile_name + ".txt", "r")
    wordlist = []
    for line in textfile:
        stripped_line = line.strip()
        wordlist.append(stripped_line)
    textfile.close
    return wordlist


def dictionary_build(wordlist):
    ''' Returns: Dictionary of dictionaries, word length -> word position. '''
    length_longest_word = len(max(wordlist, key=len))
    length_dictionary = {str(i+1): {str(j+1): [] for j in range(i+1)}
                         for i in range(length_longest_word)}
    for word in wordlist:
        length = len(word)
        for position in range(length):
            length_dictionary[str(length)][str(
                position + 1)].append(word[position])
    return length_dictionary


def alt_dictionary(wordlist):
    data = {}
    for word in wordlist:
        view = data
        for letter in word:
            if letter not in view:
                view[letter] = {"count": 0, "cross": 0}
            view[letter]["cross"] += 1
            view = view[letter]
        view["count"] += 1
    print(data)
    print(data["a"]["l"]["p"]["h"]["a"])

def word_analysis(textfile_name):
    ''' Returns: . '''
    wordlist = load_words(textfile_name)
    length_dictionary = alt_dictionary(wordlist)
    print(json.dumps(length_dictionary, indent=2))


word_analysis("corncob_lowercase")
