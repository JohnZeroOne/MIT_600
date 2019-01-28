# 6.00 Problem Set 3
# 
# Hangman
#
# Name: Jane Lee
# Collaborators (Discussion): none
# Collaborators (Identical Solution): none
# Time: 7h

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string
#old
#import re

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

# your code begins here!

def hangman():
    """
    starts the game

    initializes variables

    displays info to user
    """
    # choose a random word from the text file
    ans_word = random.choice(wordlist)
    num_guesses = 8
    # store alphabetical list to show user picked letter
    lettersLst = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    # show the users progress with a word that matches the answer length
    progressLst = len(ans_word) * ["_"]
    
    print "Welcome to the Hangman game!"
    # for testing
    ## print "Dev. testing, answer is:", ans_word
    print "The word is", len(ans_word), "letters long"
    print "-----------"
    take_turn(progressLst, lettersLst, ans_word, num_guesses)
    
def take_turn(progressLst, lettersLst, ans_word, num_guesses):
    """
    iterates over one turn

    takes user input of 1 letter and applies error correction
    
    checks if user guess is in the answer and calls appropriate function
    """
   
    print "You have", num_guesses, "guesses left."
    print "Current progress:", (" ".join(progressLst))
    print "Available letters:", (", ".join(lettersLst))
    print "-----------"
    # let the user guess a letter in the word
    guess = raw_input("Pick 1 letter from above as your guess: ")
    # error correct user input
    # length
    if len(guess)!= 1:
        print "Your input should be 1 letter"
        print "-----------"
        take_turn(progressLst, lettersLst, ans_word, num_guesses)
    # convert to lowercase to ensure it matches
    guess = guess.lower()
    # character set
    if guess not in lettersLst:
        print "This letter is not available, pick again"
        print "-----------"
        take_turn(progressLst, lettersLst, ans_word, num_guesses)
    # passed error correction
    else:
        # remove guess from available letters
        lettersLst.remove(guess)
        # compare guess with answer word
        if guess in ans_word:
            print "Good guess:"
            print "-----------"
            letter_helper(guess, progressLst, lettersLst, ans_word, num_guesses)
        else:
            num_guesses -= 1
            print "Uh oh, that letter is not in the answer:", (" ".join(progressLst))
            print "-----------"
            progress(progressLst, lettersLst, ans_word, num_guesses)

def letter_helper(guess, progressLst, lettersLst, ans_word, num_guesses):
    """
    take the users guess and adds it to progress word
    """
    
    for position, letter in enumerate(ans_word):
        if letter == guess:
            progressLst[position] = letter

#    print "testing, progressLst:", progressLst

# deprecated
##    temp = re.sub(guess, '!', ans_word)
##    print "testing, temp", temp
##    temp2 = re.sub('[^!]', '_', temp)
##    print "testing, temp", temp2
##    temp3 = re.sub('!', guess, temp2)
##    print "testing, temp", temp3
##    return False

    progress(progressLst, lettersLst, ans_word, num_guesses)


def progress(progressLst, lettersLst, ans_word, num_guesses):
    """
    check if the player has won

    check if they have remaining guesses

    otherwise they lose and the game restarts
    """
    # temporary answer check
    answer = ""
    answer = ''.join(progressLst)
    # win condition
    if answer == ans_word:
        print "Your guess:", answer
        print "The correct answer is:", ans_word
        print "Congratulations, you win!"
        print "GAME OVER"
        print "-----------"
        hangman()
    # loss condition
    elif num_guesses <= 0:
        print "Your guess:", answer
        print "The answer was:", ans_word
        print "Unfortunately, you lose!"
        print "GAME OVER"
        print "-----------"
        hangman()
    # turns remaining
    else:
        take_turn(progressLst, lettersLst, ans_word, num_guesses)
# start
hangman()
