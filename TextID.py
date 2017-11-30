#
# milestone.py
# TextID
# Names: Rakia Segev and Anisha Tandon
#

from collections import defaultdict
from porter import create_stem

TextModel1 = [ ]  # start with the empty list

words1 = defaultdict( int )  # default dictionary for counting
TextModel1 = TextModel1 + [ words1 ]  # add that dictionary in...

wordlengths1 = defaultdict( int )  # default dictionary for counting
TextModel1 = TextModel1 + [ wordlengths1 ]  # add that dictionary in...

stems1 = defaultdict( int )  # default dictionary for counting
TextModel1 = TextModel1 + [ stems1 ]  # add that dictionary in...

sentencelengths1 = defaultdict( int )  # default dictionary for counting
TextModel1 = TextModel1 + [ sentencelengths1 ]  # add that dictionary in...

complexity1 = defaultdict( int )
TextModel1 = TextModel1 + [complexity1]  # add that dictionary in...

# a function to print all of the dictionaries in a TextModel1

def printAllDictionaries( TM ):
    """ a function to print all of the dictionaries in TM
        input: TM, a text model (a list of 5 or more dictionaries)
    """
    words = TM[0]
    wordlengths = TM[1]
    stems = TM[2]
    sentencelengths = TM[3]

    print("The text model has these dictionaries:")
    print("\nWords:\n", words)
    print("\nWord lengths:\n", wordlengths)
    print("\nStems:\n", stems)
    print("\nSentence lengths:\n", sentencelengths)
    print("\n\n")

def readTextFromFile(filename):
    """ take in a filename as a string and create a large string out of the file"""
    f = open(filename)
    text = f.read()
    string = str(text)
    return string

def makeSentenceLengths(s):
    """ use the text in the input string s to create the sentencelength dictionary."""
    
    frequency = 0
    length = 0

    LoW = s.split() # splits the string into string of each word
    sl = [] # list of sentence lengths

    # create loop to iterate through all indices
    # check if word has .!?, if not add oen to length
    # if yes, check if length value is in dicitonary, if yest + 1 to frequency, if not add to dictionary, 1 frequency
    # continue 

    for i in LoW: 
        length += 1
        if i[-1] in '?!.':
            sl += [length]
            length = 0

    sentencelengths = {}

    for l in sl: # iterate through length (l) in the list
        if l not in sentencelengths:
            sentencelengths[l] = 1
        elif l in sentencelengths:
            sentencelengths[l] += 1
    return sentencelengths

print("TextModel1:")
printAllDictionaries( TextModel1 )


def cleanString(s): 
    """ takes in a string s and return a string with no punctuation and no upper-case letters""" 
    s = s.lower()

    import string

    for p in "?.!,'": # looping over punctuation
        s = s.replace(p,'') # replacing punctuation with space
    return s # returning new string

def makeWordLengths(s): 
    """ uses the text in the input string s to create the self.wordlengths dictionary"""

    s = cleanString(s) # removing punctuation 
    
    LoW = s.split() # splits the string into string of each word
    wl = [] #list of word lengths

    for word in LoW: 
        wl += [len(word)] # adds each length of word

    wordlengths = {}

    for l in wl: # iterate through length (l) in the list
        if l not in wordlengths:
            wordlengths[l] = 1
        elif l in wordlengths:
            wordlengths[l] += 1
    return wordlengths

def makeWords(s): 
    """ uses the text in the input string s to create the self.words dictionary"""
    
    s = cleanString(s) # removing punctuation 
    
    LoW = s.split() # splits the string into string of each word
    
    wordlengths = {}

    for l in LoW: # iterate through words in the list
        if l not in wordlengths:
            wordlengths[l] = 1 # if not in dictionary add
        elif l in wordlengths:
            wordlengths[l] += 1 # if in dictionary add to number
    return wordlengths

def makeStems(s): 
    """uses the text in the input string s to create the self.stems dictionary"""
    s = cleanString(s) # removing punctuation 
    
    LoW = s.split() # splits the string into string of each word
    
    stl = [] # create empty array of to be stems

    for w in LoW: 
        stl += [create_stem(w)] # create stem word for every word in string from test
    
    stems = {}

    for l in stl: # iterate through words in the list
        if l not in stems:
            stems[l] = 1 # if not in dictionary add
        elif l in stems:
            stems[l] += 1 # if in dictionary add to number
    return stems

def makePunctuation(s): 
    "use the text in the input string s to create and return the punctuation dictionary"""    
    
    LoW = list(s) # splits the string into string of each word
    
    pl = [] # empty array to put punctuation into 

    for punctuation in LoW: 
        if punctuation in "!.?,'": # check if an index is a punctuation
            pl += [punctuation]

    print(pl)

    punctuationdictionary = {}

    for p in pl: # iterate through punctuation in the array
        if p not in punctuationdictionary:
            punctuationdictionary[p] = 1 # if not in dictionary add
        elif p in punctuationdictionary:
            punctuationdictionary[p] += 1 # if in dictionary add to number
    return punctuationdictionary
