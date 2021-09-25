A simple word checking program that gives suggestions for words that are exactly one edit away from the wrong word.
Uses a set that contains all of the words in a dictionary for processing power.
The contains method checks if a specific word is in the set.
The getSuggestions method produces a list of words that are "nearby" words (one edit away from the incorrect word).
There are exhaustive test cases to check and make sure every piece of the code works.
In order to generate the list of nearby words, we found string splicing worked best. When I first tried to manipulate the words with lists, I found it to be rather slow and difficult.

Credits:
translator = str.maketrans('', '', string.punctuation) : https://stackoverflow.com/questions/34293875/how-to-remove-punctuation-marks-from-a-string-in-python-3-x-using-translate

Worked on with Alexander Juan

