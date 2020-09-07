# Hangman game


import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
  
    inFile = open(WORDLIST_FILENAME, 'r')
    
    line = inFile.readline()
 
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
   
    if len(lettersGuessed) == 0:
        return False
 
    for letters in secretWord:
        for words in lettersGuessed:
            if letters not in lettersGuessed:
                return False
    return True



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
   
    guessedWord = []
    for letters in secretWord:
        if letters in lettersGuessed:
            guessedWord.append(letters)
        else:
            guessedWord.append("_" + " ")
    return ''.join(guessedWord)

                



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for letters in lettersGuessed:
        for letter in alphabet:
            if letters in alphabet:
                alphabet.remove(letters)
    return ''.join(alphabet)    

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
   
    print("Welcome to the game hangman!")
    wordLen = len(secretWord)
    print("I am thinking of a word that is " + str(wordLen) + " " + "letters long.")
    count = wordLen + 5
    lettersGuessed = []
    print("-----------")
    while(count > 0):
        availableLetters = getAvailableLetters(lettersGuessed)
       
        print("You have " + str(count) + " " + "guesses left")
        
        print("Available letters are " + availableLetters)
        
        guess = input("Please guess a letter: ")
        guessInLowerCase = guess.lower()
        
        lettersGuessed.append(guessInLowerCase)
        
        if guessInLowerCase not in availableLetters:
            print("Oops! You've already guessed that letter." + getGuessedWord(secretWord, lettersGuessed))
            count += 1
        elif guessInLowerCase in secretWord:
            print("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
            count += 1
        else:
            print("Oops! That letter is not in my word " + getGuessedWord(secretWord, lettersGuessed))
       
        print("-----------")
        
        if isWordGuessed(secretWord, lettersGuessed) == True:
            print("Congratulations! You guessed the word!")
            break
        count -= 1
    if isWordGuessed(secretWord, lettersGuessed) == False:
        print("Sorry you ran out of guesses, the word is: " + secretWord)
        
    

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
