from collections import defaultdict

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
    ''' Returns: Dictionary tree number words. '''
    data = defaultdict(int)
    for word in wordlist:
        for position, letter in enumerate(word):
            if position == 0:
                previous = ""
            else:
                previous = word[:position]
            data[len(word), position, previous, letter] += 1
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
    letter_probability = probability(word_dictionary, 5, 0, "")
    print(letter_probability)

word_analysis("corncob_lowercase")
