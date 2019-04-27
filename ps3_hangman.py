# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    result=1
    for l in secretWord:
        if l in lettersGuessed:
            result*=1
        else:
            result*=0
    if result==0:
        return False
    elif result==1:
        return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    result="_"*len(secretWord)
    for guess in lettersGuessed:
        for index,l in enumerate(secretWord):
            if l==guess:
                result=result[0:index]+l+result[index+1:]
    return result


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    lettersAvailable=''
    for letter in string.ascii_lowercase:
        if letter not in lettersGuessed:
            lettersAvailable=lettersAvailable+letter
    return lettersAvailable

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is ",len(secretWord)," letters long")
    print("___________")
    game=True
    numberOfTriesLeft=8
    lettersGuessed=[]
    while game:
        print("You have ",numberOfTriesLeft," guesses left.")
        print("Available letters: ",getAvailableLetters(lettersGuessed))
        guess=input("Please guess a letter: ").lower()
        if guess in lettersGuessed:
            print("Oops! You've already guessed that letter: ", getGuessedWord(secretWord, lettersGuessed))
            print("___________")
        else:
            lettersGuessed.append(guess)
            if guess in secretWord:
                print("Good guess: ",getGuessedWord(secretWord, lettersGuessed))
                print("___________")
            else:
                numberOfTriesLeft-=1
                print("Oops! That letter is not in my word: ",getGuessedWord(secretWord, lettersGuessed))
                print("___________")
        if "_" not in getGuessedWord(secretWord, lettersGuessed):
            print("Congratulations, you won!")
            game=False
        elif numberOfTriesLeft==0:
            print("Sorry, you ran out of guesses. The word was ",secretWord,".")            
            game=False





# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
