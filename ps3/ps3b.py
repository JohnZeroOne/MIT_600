from ps3a import *
import time
from perm import *


#
#
# Problem #6A: Computer chooses a word
#
# 70m
def comp_choose_word(hand, word_list):
    """
	Given a hand and a word_list, find the word that gives the maximum value score, and return it.
   	This word should be calculated by considering all possible permutations of lengths 1 to HAND_SIZE.

    hand: dictionary (string -> int)
    word_list: list (string)
    """
    ## comp_choose_word({'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}, word_list)
    # print "processing words.."
    # make a list of all permutations of the hand, max length
    char_len = len(hand)
    # allow to iterate max length
    char_len += 2
    # iterate through all permutations reducing length by 1 until we find a word
    while char_len > 0:
        char_len -= 1
        perm_list = get_perms(hand, char_len)
        for word in perm_list:
            if word in word_list:
                return word
    return None
            
#
# Problem #6B: Computer plays a hand
#
# 30m
def comp_play_hand(hand, word_list):
    """
     Allows the computer to play the given hand, as follows:

     * The hand is displayed.

     * The computer chooses a word using comp_choose_words(hand, word_dict).

     * After every valid word: the score for that word is displayed, 
       the remaining letters in the hand are displayed, and the computer 
       chooses another word.

     * The sum of the word scores is displayed when the hand finishes.

     * The hand finishes when the computer has exhausted its possible choices (i.e. comp_play_hand returns None).

     hand: dictionary (string -> int)
     word_list: list (string)
    """
    #comp_play_hand({'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}, word_list)
    
    total_score = 0

    while HAND_SIZE > 0:

        # show user hand
        print "Current hand: ", display_hand(hand)
        # compute largest available word
        word = comp_choose_word(hand, word_list)
        if word == None:
            break
        # use letters from hand
        update_hand(hand, word)
        # show score
        score = get_word_score(word, HAND_SIZE)
        # update total for each word
        total_score += score
        print "'", word, "'", "scored", score, "points.", "Total:", total_score
 
    # show sum score for hand
    print "Total score: ", total_score
    return total_score
    
#
# Problem #6C: Playing a game
#
# 20m
def play_game(word_list):
    """Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
    * If the user inputs 'n', play a new (random) hand.
    * If the user inputs 'r', play the last hand again.
    * If the user inputs 'e', exit the game.
    * If the user inputs anything else, ask them again.

    2) Ask the user to input a 'u' or a 'c'.
    * If the user inputs 'u', let the user play the game as before using play_hand.
    * If the user inputs 'c', let the computer play the game using comp_play_hand (created above).
    * If the user inputs anything else, ask them again.

    3) After the computer or user has played the hand, repeat from step 1

    word_list: list (string)
    """
    
    #2)
    def user_comp(nr):
        print "Do you want to play the game or let the computer play?"
        print "Enter u for user, or c for computer: "
        user_input = raw_input()
        if user_input == 'u':
            # new hand
            play_hand(deal_hand(HAND_SIZE), word_list)
        elif user_input == 'c':
            comp_play_hand(deal_hand(HAND_SIZE), word_list)
        else:
            print "Invalid input"
        play_game(word_list)
            

    # need to restart game once hand size is 0
    # need to implement replay last hand

    #1)
    print "Please enter one of the following: "
    print "n - to play a new random hand"
    print "r - to repeat the last hand you played - not implemented"
    print "e - to exit the game"
    user_input = raw_input()
    if user_input == 'n':
        user_comp('n')
    elif user_input == 'r':
        # not sure how to implement this without making hand global and changing all of program
        user_comp('r')
    elif user_input == 'e':
        print "GAME OVER"
    else:
        print "Invalid input"

        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)

    
