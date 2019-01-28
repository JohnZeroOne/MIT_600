# 6.00 Problem Set 3A Solutions
#
# The 6.00 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
#

import random
import string
import copy

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

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
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print "  ", len(wordlist), "words loaded."
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
# 2h
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

	The score for a word is the sum of the points for letters
	in the word multiplied by the length of the word, plus 50
	points if all n letters are used on the first go.

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string (lowercase letters)
    returns: int >= 0
    """
    # store score progress
    score = 0
    # iterate letters and add to score
    for letter in word:
        # lookup letter in dict
        if letter in SCRABBLE_LETTER_VALUES:
            #print "letter value: %s" % SCRABBLE_LETTER_VALUES.get(letter)
            score += SCRABBLE_LETTER_VALUES.get(letter)
    score = score * len(word)
    if len(word) == n:
        score += 50
    assert score >= 0
    return score
    
#
# Make sure you understand how this function works and what it does!

def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print letter,              # print all on the same line
    print                               # print an empty line

#
# Make sure you understand how this function works and what it does!
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    num_vowels = n / 3
    
    for i in range(num_vowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(num_vowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

#
# Problem #2: Update a hand by removing letters
# 1 hour
def update_hand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
	In other words, this assumes that however many times
	a letter appears in 'word', 'hand' has at least as
	many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    #test
    # print "Entry hand: ", hand
    # iterate each letter of word
    for letter in word:
        # search dict for letter
        if letter in hand:
##            # show presence
##            # print "True, letter: ", letter
##            # remove letter from dict, not working as intended
##            # hand.pop(letter, None)
            
            # reduce value by 1 for each letter
            hand[letter] -= 1
            
            #test
    # print "Exit hand: ", hand
    return hand

#
# Problem #3: Test word validity
#
# 50m
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
    
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    """
##    while True:
##        # check the word is in our list
##        if word in word_list:
##            print "word in word list: True"
##        else:
##            print "word in word list: False"
##            return False
##        # check the letters are in the hand
##        for letter in word:
##            if letter in hand:
##                print "letter in word: True"
##            else:
##                print "letter in word: False"
##                return False
##        return True
    
    # copy dict so we can modify values
    hand2 = copy.deepcopy(hand)
    # TEST: show copy integrity
    # print "hand2 copy", hand2
    
    # check the word is in our list
    if word not in word_list:
        return False
    # check the letters are in our hand
    for letter in word:
        if letter in hand2:
            # remove 1 from value for each letter
            hand2[letter] -= 1
            # if value is 0 remove that letter from our dict copy
            if hand2[letter] <= 0:
                hand2.pop(letter, None)
        # stop if letters arent in hand
        else:
            return False
    # TEST
    # print "check hand integrity", hand
    return True

def calculate_handlen(hand):
    handlen = 0
    for v in hand.values():
        handlen += v
    return handlen

#
# Problem #4: Playing a hand
#
# 50m
def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * When a valid word is entered, it uses up letters from the hand.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing a single
      period (the string '.') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      
    """
    # while letters are remaining
    total_score = 0

    while HAND_SIZE > 0:

        # show user hand
        print "Current hand: ", display_hand(hand)
        ## where is None coming from?
        # take word input from user or "."
        word = raw_input("Enter word, or a '.' to indicate that you are finished: ")
        # end turn if user enters .
        if word == '.':
            break
        # check word is valid
        if is_valid_word(word, hand, word_list):
            # valid pass
            # use letters from hand
            update_hand(hand, word)
            # show score
            score = get_word_score(word, HAND_SIZE)
            # update total for each word
            total_score += score
            print "'", word, "'", "scored", score, "points.", "Total:", total_score
        else:
            print "Invalid word, please try again."
        ## where is hand_size incrementing?
        # loop back to start

    # show sum score for hand
    print "Total score: ", total_score
    return total_score

#
# Problem #5: Playing a game
# Make sure you understand how this code works!
#
# 20m
def play_game(word_list):
    """
    Allow the user to play an arbitrary number of hands.

    * Asks the user to input 'n' or 'r' or 'e'.

    * If the user inputs 'n', let the user play a new (random) hand.
      When done playing the hand, ask the 'n' or 'e' question again.

    * If the user inputs 'r', let the user play the last hand again.

    * If the user inputs 'e', exit the game.

    * If the user inputs anything else, ask them again.
    """
    # not sure this loop does what I want
    # while HAND_SIZE == 0:
        
    print "Please enter one of the following: "
    print "n - to play a new random hand"
    print "r - to repeat the last hand you played - not implemented"
    print "e - to exit the game"
    user_input = raw_input()
    if user_input == 'n':
        # new hand
        play_hand(deal_hand(HAND_SIZE), word_list)
    elif user_input == 'r':
        # not sure how to implement this without making hand global and changing all of program
        # replay last hand
        play_hand(deal_hand(HAND_SIZE), word_list)
    elif user_input == 'e':
        print "GAME OVER"
    else:
        print "Invalid input"
    play_game(word_list)

    # need to restart game once hand size is 0
    # need to implement replay last hand

#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
