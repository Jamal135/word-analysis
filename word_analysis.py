''' Created: 13/08/2022 '''

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
    return set(wordlist)


def dictionary_build(wordlist: list):
    ''' Returns: Dictionary tree next letter frequency. '''
    data = defaultdict(int)
    for word in tqdm(wordlist):
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


build_dataframe("words_short")
build_dataframe("words_long")


def load_CSV(filename: str):
    ''' Returns: CSV loaded to dataframe. '''
    if not filename.endswith(".csv"):
        filename += ".csv"
    return read_csv(filename)


def dataframe_extract(dataframe, length: list, position: list, previous: list):
    ''' Returns: Dataframe cut to desired rows. '''
    if not length:
        length = dataframe["Length"].unique()
    if not position:
        position = dataframe["Position"].unique()
    if not previous:
        previous = dataframe["Previous"].unique()
    dataframe = dataframe[dataframe["Length"].isin(length) &
                          dataframe["Position"].isin(position) &
                          dataframe["Previous"].isin(previous)]
    return dataframe


def word_analysis(length: list, position: list, previous: list, datafile: str = "words_short"):
    ''' Returns: The percentage chance of each next letter given arguments. '''
    dataframe = load_CSV(datafile)
    cut_dataframe = dataframe_extract(dataframe, length, position, previous)
    print(frequency(cut_dataframe))


word_analysis([], [], ["a", "b"], "words_long")