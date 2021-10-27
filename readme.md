# Letter Probability Word Analysis Tool

***
# About:
---

Originally this code was written to create a comprehensive lookup table that can be utilised in testing a new approach to text data compression. This having been said, it turns out that exploring the probabilities of different letters given different known factors is pretty interesting. As a result of this, I have made this code available as a fun little stand alone repository.

Creation Date: 27/10/2021

***
# Usage:
--- 

The following arguments can be provided when calling the word_analysis function:

* Length: An integer list describing the number of characters in the word.
* Position: An integer list describing the index position within the word.
* Previous: A string list describing which previous characters must exist.

User beware, this code currently has no error correction and it is on you to provide correct arguments. Examples include, position index should not exceed minimum length input minus one and an empty string should never be provided for the previous input.

## No Arguments:

Providing no argument for input means any value is allowed for that input. For example, no argument for length means all words from the shortest length to the longest will be included in the letter probability calculations. In the case of 

```python
word_analysis([], [], [])
```

Output:
```
[('e', 12.38), ('s', 10.17), ('i', 9.47), ('n', 8.22), ('t', 7.84), ('a', 6.8), ('r', 6.61), ('l', 5.94), ('o', 5.43), ('d', 4.22), ('g', 3.56), ('c', 3.4), ('u', 2.63), ('y', 2.59), ('m', 2.11), ('p', 1.92), ('h', 1.74), ('b', 1.36), ('f', 0.92), ('v', 0.91), ('k', 0.77), ('w', 0.53), ('x', 0.19), ('z', 0.11), ('q', 0.1), ('j', 0.07)]
```

## Single Arguments:

Given the provided arguments, we are calculating the most likely next letter given the word is five characters long, this letter is in the fifth position, and the previous two letters were "ba". In this case, "ba" must form the third and four letter (in that order) of any word for it to be included in the probability calculation. Additionally, that word must be exactly five characters long. Note: position starts at zero, so the fourth position is the fifth character.

```python
word_analysis([5], [4], ["ba"])
```

Output:
```
[('s', 22.22), ('r', 22.22), ('n', 22.22), ('t', 11.11), ('l', 11.11), ('b', 11.11), ('z', 0.0), ('y', 0.0), ('x', 0.0), ('w', 0.0), ('v', 0.0), ('u', 0.0), ('q', 0.0), ('p', 0.0), ('o', 0.0), ('m', 0.0), ('k', 0.0), ('j', 0.0), ('i', 0.0), ('h', 0.0), ('g', 0.0), ('f', 0.0), ('e', 0.0), ('d', 0.0), ('c', 0.0), ('a', 0.0)]

```
## List Arguments:

For completion, it should also be noted that arguments can be provided as lists. With the given example below, we are doing the probability calculations using a word that is any length between five characters and eight.

```python
word_analysis([5, 6, 7, 8], [1], ["a"])
```

Output:
```
[('n', 11.47), ('l', 10.11), ('r', 9.93), ('d', 8.68), ('c', 7.91), ('b', 7.79), ('s', 7.25), ('m', 5.95), ('p', 5.59), ('u', 4.04), ('t', 3.86), ('i', 3.75), ('g', 2.97), ('v', 2.85), ('f', 2.5), ('w', 1.55), ('e', 1.49), ('x', 0.71), ('q', 0.65), ('z', 0.42), ('o', 0.24), ('a', 0.18), ('k', 0.06), ('h', 0.06), ('y', 0.0), ('j', 0.0)]
```
***
# Acknowledgements:
---

This project was a first for me in terms of using Pandas Dataframes and generating/navigating such a large amount of data. Given this, the guidance of some awesome individuals from the official Python Discord was instrumental in enabling the development of this code. It must also be acknowledged that this project would not of been possible without the publicly available word list from Mieliestronk's website.

Join Official Python Discord: https://discord.gg/python
Mieliestronk's Word List: http://www.mieliestronk.com/wordlist.html 

***
# Future:
---

At a later date this tool may be developed to account for word popularity. Additionally, this tool might be expanded upon to allow specification of any known letters in any position as this will make a cool cheat tool for Hangman.

***
# License:
--- 
MIT License