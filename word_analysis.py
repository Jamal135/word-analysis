from pandas import DataFrame, Series
from collections import defaultdict

def load_words(txt_name: str):
    ''' Returns: Loaded list of words from txt. '''
    textfile = open(txt_name + ".txt", "r")
    wordlist = []
    for line in textfile:
        stripped_line = line.strip()
        wordlist.append(stripped_line)
    textfile.close
    return wordlist

def dictionary_build(wordlist: list):
    ''' Returns: Dictionary tree next letter frequency. '''
    data = defaultdict(int)
    for word in wordlist:
        for position, letter in enumerate(word):
            previous = word[:position + 1]
            length = len(word)
            for point, _ in enumerate(previous):
                segment = previous[point:position]
                data[length, position, segment, letter] += 1
    return data

def dataframe_build(data: dict):
    ''' Returns: Built and named dataframe from dictionary. '''
    dataframe = DataFrame.from_records(Series(data).reset_index())
    dataframe.rename(columns={'level_0': 'Length', 'level_1': 'Position',
                              'level_2': 'Previous', 'level_3': 'Letter',
                              0: 'Count'}, inplace=True)
    return dataframe

def dataframe_extract(dataframe, length: list, position: list, previous: list):
    ''' Returns: Dataframe cut to desired rows. '''
    if length == []:
        length = dataframe["Length"].unique()
    if position == []:
        position = dataframe["Position"].unique()
    if previous == []:
        previous = dataframe["Previous"].unique()
    dataframe = dataframe[dataframe["Length"].isin(length) &
                          dataframe["Position"].isin(position) &
                          dataframe["Previous"].isin(previous)]
    return dataframe

def frequency(dataframe):
    ''' Returns: Sorted count and probability of each letter. '''
    characters = "abcdefghijklmnopqrstuvwxyz"
    letter_data = defaultdict(int)
    total_count = dataframe["Count"].sum()
    for letter in characters:
        rows = dataframe[dataframe["Letter"].isin([letter])]
        count = sum(rows['Count'])
        letter_data[letter] += round((100/total_count)*count, 2)
    return (sorted(letter_data.items(), key = lambda ab:(ab[1], ab[0]), reverse=True)) 

def word_analysis(txt_name: str, length: list, position: list, previous: list):
    ''' Returns: The percentage chance of each next letter given arguments. '''
    wordlist = load_words(txt_name)
    word_dictionary = dictionary_build(wordlist)
    dataframe = dataframe_build(word_dictionary)
    cut_dataframe = dataframe_extract(dataframe, length, position, previous)
    return frequency(cut_dataframe)
