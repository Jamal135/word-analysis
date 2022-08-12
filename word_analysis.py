''' Creation Date: 27/10/2021 '''

from distutils.command.build import build
from pandas import DataFrame, Series, read_csv
from collections import defaultdict
from tqdm import tqdm


def load_words(textfile_name: str):
    """ Returns: Loaded list of words from txt. """
    textfile = open(textfile_name, "r")
    wordlist = []
    for line in tqdm(textfile):
        stripped_line = line.strip()
        wordlist.append(stripped_line)
    textfile.close
    return wordlist


def dictionary_build(wordlist: list):
    ''' Returns: Dictionary tree next letter frequency. '''
    data = defaultdict(int)
    for word in tqdm(wordlist):
        length = len(word)
        for index in range(length):
            letter = word[index]
            previous = word[:index]
            following = word[index + 1:]
            for cut in range(len(previous) + 1):
                a = previous[cut:]
                for cut in range(len(following) + 1):
                    b = following[:cut]
                    data[length, index, a, b, letter] += 1
    return data


def dataframe_build(data: dict):
    ''' Returns: Built and named dataframe from dictionary. '''
    dataframe = DataFrame.from_records(Series(data).reset_index())
    dataframe.rename(columns={'level_0': 'Length', 'level_1': 'Position',
                              'level_2': 'Previous', 'level_3': 'Following',
                              'level_4': 'Letter', 0: 'Count'}, inplace=True)
    return dataframe


def frequency(dataframe):
    ''' Returns: Sorted count and probability of each letter. '''
    characters = "abcdefghijklmnopqrstuvwxyz"
    letter_data = defaultdict(int)
    total_count = dataframe["Count"].sum()
    if total_count == 0: 
        return None
    for letter in characters:
        rows = dataframe[dataframe["Letter"].isin([letter])]
        count = sum(rows['Count'])
        letter_data[letter] += round((1/total_count)*count, 4)
    return (sorted(letter_data.items(), key = lambda ab:(ab[1], ab[0]), reverse=True)) 


def build_dataframe(output_name: str, textfile_name: str = None):
    """ Returns: Created CSV file frequency analysis given textfile. """
    if textfile_name is None:
        textfile_name = output_name
    if not textfile_name.endswith(".txt"):
        textfile_name += ".txt"
    print(f"Loading Words: {textfile_name}")
    wordlist = load_words(textfile_name)
    word_dictionary = dictionary_build(wordlist)
    dataframe = dataframe_build(word_dictionary)
    if not output_name.endswith(".csv"):
        output_name += ".csv"
    print(f"Saving Dataframe: {output_name}")
    dataframe.to_csv(output_name, index=False)


def load_CSV(filename: str):
    ''' Returns: CSV loaded to dataframe. '''
    if not filename.endswith(".csv"):
        filename += ".csv"
    return read_csv(filename)


def dataframe_extract(dataframe, length: list, position: list, 
                      previous: list, following: list):
    ''' Returns: Dataframe cut to desired rows. '''
    if not length:
        length = dataframe["Length"].unique()
    if not position:
        position = dataframe["Position"].unique()
    if not previous:
        previous = dataframe["Previous"].unique()
    if not following:
        following = dataframe["Following"].unique()
    dataframe = dataframe[dataframe["Length"].isin(length) &
                          dataframe["Position"].isin(position) &
                          dataframe["Previous"].isin(previous) &
                          dataframe["Following"].isin(following)]
    return dataframe


def word_analysis(length: list, position: list, previous: list, following: list, 
                  datafile: str = "words_short"):
    ''' Returns: The percentage chance of each next letter given arguments. '''
    dataframe = load_CSV(datafile)
    cut_dataframe = dataframe_extract(dataframe, length, position, previous, following)
    print(frequency(cut_dataframe))


# Find probability letters given any position, any length where previous chars are a & b and following is a.
word_analysis([], [], ["a", "b"], ["a"], "words_long")