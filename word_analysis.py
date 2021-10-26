from collections import defaultdict
from re import search

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
    ''' Returns: Dictionary tree next letter frequency. '''
    data = defaultdict(int)
    for word in ['time', 'times']:
        for position, letter in enumerate(word):
            previous = word[:position + 1]
            for point, _ in enumerate(previous):
                data[len(word), position, previous[:point], letter] += 1
                #data[len(word), "", previous[:point], letter] += 1
                #data["", position, previous[:point], letter] += 1
                #data["", "", previous[:point], letter] += 1
    print(data)
    return data

def probability(input_data, length, position, previous):
    ''' Returns: Probability each letter given arguments. '''
    characters = "abcdefghijklmnopqrstuvwxyz"
    data = defaultdict(int)
    for letter in characters:
        data[letter] = input_data[length, position, previous, letter]
    return data

def word_analysis(textfile_name):
    ''' Returns: . '''
    wordlist = load_words(textfile_name)
    word_dictionary = dictionary_build(wordlist)
    letter_probability = probability(word_dictionary, 6, 1, 'a')
    print(letter_probability)
    letter_probability = probability(word_dictionary, "", 2, 'ti')
    print(letter_probability)
    letter_probability = probability(word_dictionary, "", "", 'ti')
    print(letter_probability)

word_analysis("corncob_lowercase")
