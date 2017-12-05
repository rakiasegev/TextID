
from collections import defaultdict
from porter import create_stem

import math

from math import ceil, floor

def float_round(num, places = 0):
    return float(str(round(num, places)))
# code of float_round to round to 2 decimals


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

    for l in stl: # iterate through stems in the list
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

    punctuationdictionary = {}

    for p in pl: # iterate through punctuation in the array
        if p not in punctuationdictionary:
            punctuationdictionary[p] = 1 # if not in dictionary add
        elif p in punctuationdictionary:
            punctuationdictionary[p] += 1 # if in dictionary add to number
    return punctuationdictionary

def normalizeDictionary(d):
    """ take in any single one of the model-dictionaries d and return a normalized version, numbers adding to 1"""
    
    values = d.values() # lists value in dictionary d
    sumValues = sum(values)
  
    for k in d:
        s = d[k]/sumValues # divide value by sum of values to normalize
        d[k] = s
    return d

def smallestValue(nd1, nd2):
    """ take in any two model-dictionaries nd1 and nd2, return the smallest positive (non-zero) value across both"""
  
    valuesd1 = list(nd1.values()) # list values of each dictionary
    valuesd2 = list(nd2.values())

    if min(valuesd1) < min(valuesd2): #check which one is the smallest
        return min(valuesd1)
    else:
        return min(valuesd2)

def compareDictionaries(d, nd1, nd2):
    """ return the log-probability that the dictionary d arose from the distribution of data in the normalized dictionary nd1 and
    the log-probability that dictionary d arose from the distribution of data in normalized dictionary nd2 and return both values"""

    total_log_prob1 = 0.0
    total_log_prob2 = 0.0 # initializing probability to zero
    epsilon = 0.5*smallestValue(nd1, nd2) # creating an epsilon case

    for k in d: # iterate through keys in the dictionary
        if k in nd1:
            total_log_prob1 += d[k]*math.log(nd1[k]) # if it is in the dictionary, compute log probability
        else:
            total_log_prob1 += d[k]*math.log(epsilon) # otherwise use epsilon

    for k in d:
        if k in nd2: # repeating loop for second dictionary
            total_log_prob2 += d[k]*math.log(nd2[k])
        else:
            total_log_prob2 += d[k]*math.log(epsilon)
    
    return [total_log_prob1, total_log_prob2]

def createAllDictionaries(s): 
        """ should create out all five of self's dictionaries in full - for testing and 
            checking how they are working """
        sentencelengths = makeSentenceLengths(s) 
        new_s = cleanString(s)
        words = makeWords(new_s) #creates words dictionary
        stems = makeStems(new_s) # creates stems dictionary 
        punct = makePunctuation(s) # creates punctuation dictionary
        wordlengths = makeWordLengths(new_s) # creates word lengths dictionaries
        return [words, wordlengths, stems, sentencelengths, punct ]

def compareTextWithTwoModels(newmodel, model1, model2):
    """ run compareDictionaries for all features in dictionaries newmodel, model1, and model2 """ 

    print("SUMMARY OF COMPARISON:")
    print(" ")
    print("name            vsModel1    vsModel2")
    print("____________________________________________")

    newmodel = createAllDictionaries(readTextFromFile(newmodel)) #creating the dictionaries from input text
    model1 = createAllDictionaries(readTextFromFile(model1))
    model2 = createAllDictionaries(readTextFromFile(model2))

    for i in range(5):
        normalizeDictionary(model1[i])
        normalizeDictionary(model2[i])

    R0 = compareDictionaries(newmodel[0], model1[0], model2[0]) # comparing the values for first dictionary generated
    print("words           ", float_round(R0[0], 2), "   ", float_round(R0[1], 2) ) #printing results of comparison

    R1 = compareDictionaries(newmodel[1], model1[1], model2[1])
    print("wordlengths     ", float_round(R1[0], 2), "   ", float_round(R1[1], 2) )
    
    R2 = compareDictionaries(newmodel[2], model1[2], model2[2])
    print("stems           ",  float_round(R2[0], 2), "   ", float_round(R2[1], 2))
    
    R3 = compareDictionaries(newmodel[3], model1[3], model2[3])
    print("sentencelengths ",  float_round(R3[0], 2), "     ", float_round(R3[1], 2))
    
    R4 = compareDictionaries(newmodel[4], model1[4], model2[4])
    print("punctuation     ",  float_round(R4[0], 2), "     ", float_round(R4[1], 2))

    model1features = 0 # initialize features to 0
    model2features = 0
    rows = [R0,R1,R2,R3,R4] # create array of rows (or the dictionaries) to go through

    for i in rows:
        print("")
        if i[0] > i[1]: # compares model features and awards feature to model whose value is higher
            model1features += 1
        else:
            model2features += 1

    print("Model 1 wins on", model1features, "features!") # printing out which model wins
    print("Model 2 wins on", model2features, "features!")

    if model1features > model2features: # model 1 wins with more features
        print("--- Model 1 wins!!! --- ")
    elif model1features < model2features: # model 2 wins with more features
        print("--- Model 2 wins!!! --- ")
    else: # otherwise if there is a tie, the one whose words score is higher wins
        if R0[0] > R0[1]:
            print("--- Model 1 wins!!! --- ")
        else:
            print("--- Model 2 wins!!! --- ")


