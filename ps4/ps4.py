# 6.00 Problem Set 4
#
# Caesar Cipher Skeleton
#
import string
import random

WORDLIST_FILENAME = "words.txt"

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
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
    wordlist = line.split()
    print "  ", len(wordlist), "words loaded."
    return wordlist

wordlist = load_words()

def is_word(wordlist, word):
    """
    Determines if word is a valid word.

    wordlist: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordlist.

    Example:
    >>> is_word(wordlist, 'bat') returns
    True
    >>> is_word(wordlist, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in wordlist

def random_word(wordlist):
    """
    Returns a random word.

    wordlist: list of words  
    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

def random_string(wordlist, n):
    """
    Returns a string containing n random words from wordlist

    wordlist: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([random_word(wordlist) for _ in range(n)])

def random_scrambled(wordlist, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.

    wordlist: list of words
    n: number of random words to generate and scamble
    returns: a scrambled string of n random words


    NOTE:
    This function will ONLY work once you have completed your
    implementation of apply_shifts!
    """
    s = random_string(wordlist, n) + " "
    shifts = [(i, random.randint(0, 26)) for i in range(len(s)) if s[i-1] == ' ']
    return apply_shifts(s, shifts)[:-1]

def get_fable_string():
    """
    Returns a fable in encrypted text.
    """
    f = open("fable.txt", "r")
    fable = str(f.read())
    f.close()
    return fable


# (end of helper code)
# -----------------------------------

#
# Problem 1: Encryption
# 2h30
def build_coder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation and numbers.

    shift: -27 < int < 27
    returns: dict

    Example:
    >>> build_coder(3)
    {' ': 'c', 'A': 'D', 'C': 'F', 'B': 'E', 'E': 'H', 'D': 'G', 'G': 'J',
    'F': 'I', 'I': 'L', 'H': 'K', 'K': 'N', 'J': 'M', 'M': 'P', 'L': 'O',
    'O': 'R', 'N': 'Q', 'Q': 'T', 'P': 'S', 'S': 'V', 'R': 'U', 'U': 'X',
    'T': 'W', 'W': 'Z', 'V': 'Y', 'Y': 'A', 'X': ' ', 'Z': 'B', 'a': 'd',
    'c': 'f', 'b': 'e', 'e': 'h', 'd': 'g', 'g': 'j', 'f': 'i', 'i': 'l',
    'h': 'k', 'k': 'n', 'j': 'm', 'm': 'p', 'l': 'o', 'o': 'r', 'n': 'q',
    'q': 't', 'p': 's', 's': 'v', 'r': 'u', 'u': 'x', 't': 'w', 'w': 'z',
    'v': 'y', 'y': 'a', 'x': ' ', 'z': 'b'}
    (The order of the key-value pairs may be different.)
    """

#v4
# had to look at solution
# 40m
    assert shift > -27 and shift < 27
    assert isinstance (shift, int)
    
    EncodeDict = {}
    # create string of alphabet and space
    loweralpha = string.ascii_lowercase + ' '
    upperalpha = string.ascii_uppercase + ' '
    # apply shift to alphabet
    shiftloweralpha = loweralpha[shift:] + loweralpha[:shift]
    # make an uppercase copy
    shiftupperalpha = shiftloweralpha.upper()
    # insert our alphabet into a dictionary    
    for i in range(len(loweralpha)):
        EncodeDict[loweralpha[i]] = shiftloweralpha[i]
        
    for i in range(len(upperalpha)):
        EncodeDict[upperalpha[i]] = shiftupperalpha[i]
        
    # return dictionary
    return EncodeDict

        ## attempt 1
    ##    # creat blank dict
    ##    dictCaesar = {}
    ##    # inserting values
    ##    dictCaesar[' '] = shift
    ##    
    ##    #rangeletters = "97 123"
    ##    # iterate through alphabet numerically
    ##    for i in range(97, 123):
    ##        # test range, incld. space
    ##        #print "i:", chr(i)
    ##        # map numbers to letters
    ##
    ##        # insert plaintext & cyphertext into dict
    ##        dictCaesar[chr(i)] = chr(i+3)
    ##        # test
    ##        print "dict", dictCaesar
    ##        
    ##    # make an upper case copy
    ##    upperdict = str.upper(str(dictCaesar))
    ##    print "upper", upperdict
    ##    # add it to the dict end
    ##    dictCaesar += upperdict
    ##    return dictCaesar

    ## attempt 2
    ##    # create alpha-numeric key:value dict
    ##    dictCaesar = dict(zip(range(1,27), string.ascii_lowercase))
    ##    # add space
    ##    dictCaesar[0] = ' '
    ##    print "dictCaesar:", dictCaesar
    ##    dictShift = {}
    ##    # use values dictCaesar to create new keys in new dict
    ##    for k, v in dictCaesar.items():
    ##        print ("k: %s v: %s" % (k, v))
    ##        searchKey = int(k) + shift
    ##        searchVal = 
    ##        searchDict
    ##        print "searchkey:", searchKey
    ##        assert False
    ##        for searchKey in dictCaesar.items():
    ##            print k, v
    ##        dictShift[v] = shiftKey
    ##    print "dictShift:", dictShift
    ##    assert False
    ##    for key in dictCaesar.keys():
    ##        print "key:", key
    ##        # use shift to add new values
    ##        dictShift[key] = 1 #dictCaesar.value + shift
    ##    return dictShift

    ### v3
    ##    # error handling, input integer
    ##    while isinstance(shift, int):
    ##        # create a list of the alphabet
    ##        alphabet = [" "]
    ##        alphabet += string.ascii_lowercase
    ##        #print alphabet
    ##        #print type(alphabet)
    ##        # return the same values when there's no shift
    ##        if shift == 0:
    ##            alphabet += [" "]
    ##            alphabet += string.ascii_uppercase
    ##            print "alphabet:", alphabet
    ##            # merge 2 dictionaries
    ####            dic1 = dict(zip(string.ascii_lowercase, string.ascii_lowercase))
    ####            dic2 = dict(zip(string.ascii_uppercase, string.ascii_uppercase))
    ####            dictCaesar = dic1.copy()
    ####            dictCaesar.update(dic2)
    ####            dictCaesar[' '] = ' '
    ####            dictCaesar[' '] = ' '
    ####            return dictCaesar
    ##        # count pos when shift is pos
    ##        elif shift > 0:
    ##            # insert alphabet letter by index of the shift
    ##            for letter in alphabet:
    ##                # add letter to dict value at position
    ##                # add letter to dict key at 0
    ##                dictCaesar = dict([(letter,
    ##                shift += 1
    ##                # loop to start of alphabet after end
    ##                if shift == 27:
    ##                    shift = 0
    ##            return dictd
    ##        # count neg when shift is neg
    ##        else:
    ##            for letter in alphabet:
    ##                # add letter to dict value at position
    ##                # add letter to dict key at 0
    ##                shift -= 1
    ##                if shift == -27:
    ##                    shift = 0
    ##            return dictd

def build_encoder(shift):
    """
    Returns a dict that can be used to encode a plain text. For example, you
    could encrypt the plain text by calling the following commands
    >>>encoder = build_encoder(shift)
    >>>encrypted_text = apply_coder(plain_text, encoder)
    
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation and numbers.

    shift: 0 <= int < 27
    returns: dict

    Example:
    >>> build_encoder(3)
    {' ': 'c', 'A': 'D', 'C': 'F', 'B': 'E', 'E': 'H', 'D': 'G', 'G': 'J',
    'F': 'I', 'I': 'L', 'H': 'K', 'K': 'N', 'J': 'M', 'M': 'P', 'L': 'O',
    'O': 'R', 'N': 'Q', 'Q': 'T', 'P': 'S', 'S': 'V', 'R': 'U', 'U': 'X',
    'T': 'W', 'W': 'Z', 'V': 'Y', 'Y': 'A', 'X': ' ', 'Z': 'B', 'a': 'd',
    'c': 'f', 'b': 'e', 'e': 'h', 'd': 'g', 'g': 'j', 'f': 'i', 'i': 'l',
    'h': 'k', 'k': 'n', 'j': 'm', 'm': 'p', 'l': 'o', 'o': 'r', 'n': 'q',
    'q': 't', 'p': 's', 's': 'v', 'r': 'u', 'u': 'x', 't': 'w', 'w': 'z',
    'v': 'y', 'y': 'a', 'x': ' ', 'z': 'b'}
    (The order of the key-value pairs may be different.)

    HINT : Use build_coder.
    """
    # 1 min, this function is redundant
    assert isinstance(shift, int)
    assert shift < 27
    
    return build_coder(shift)

def build_decoder(shift):
    """
    Returns a dict that can be used to decode an encrypted text. For example, you
    could decrypt an encrypted text by calling the following commands
    >>>encoder = build_encoder(shift)
    >>>encrypted_text = apply_coder(plain_text, encoder)
    >>>decrypted_text = apply_coder(plain_text, decoder)
    
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation and numbers.

    shift: 0 <= int < 27
    returns: dict

    Example:
    >>> build_decoder(3)
    {' ': 'x', 'A': 'Y', 'C': ' ', 'B': 'Z', 'E': 'B', 'D': 'A', 'G': 'D',
    'F': 'C', 'I': 'F', 'H': 'E', 'K': 'H', 'J': 'G', 'M': 'J', 'L': 'I',
    'O': 'L', 'N': 'K', 'Q': 'N', 'P': 'M', 'S': 'P', 'R': 'O', 'U': 'R',
    'T': 'Q', 'W': 'T', 'V': 'S', 'Y': 'V', 'X': 'U', 'Z': 'W', 'a': 'y',
    'c': ' ', 'b': 'z', 'e': 'b', 'd': 'a', 'g': 'd', 'f': 'c', 'i': 'f',
    'h': 'e', 'k': 'h', 'j': 'g', 'm': 'j', 'l': 'i', 'o': 'l', 'n': 'k',
    'q': 'n', 'p': 'm', 's': 'p', 'r': 'o', 'u': 'r', 't': 'q', 'w': 't',
    'v': 's', 'y': 'v', 'x': 'u', 'z': 'w'}
    (The order of the key-value pairs may be different.)

    HINT : Use build_coder.
    """
    # 1 min
    
    # apply coder backwards to reverse it
    return build_coder(-shift)

    # Same as above but without calling coder
    ##    DecodeDict = {}
    ##    # create string of alphabet and space
    ##    loweralpha = string.ascii_lowercase + ' '
    ##    upperalpha = string.ascii_uppercase + ' '
    ##    # shift alphabet in new var
    ##    shiftloweralpha = loweralpha[-shift:] + loweralpha[:-shift]
    ##    # make an uppercase copy of shift
    ##    shiftupperalpha = shiftloweralpha.upper()
    ##    # iterate length of alphabet    
    ##    for i in range(len(shiftloweralpha)):
    ##        DecodeDict[loweralpha[i]] = shiftloweralpha[i]
    ##        DecodeDict[upperalpha[i]] = shiftupperalpha[i]
    ##    # return dictionary
    ##    return DecodeDict
 

def apply_coder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text

    Example:
    >>> apply_coder("Hello, world!", build_encoder(3))
    'Khoor,czruog!'
    >>> apply_coder("Khoor,czruog!", build_decoder(3))
    'Hello, world!'
    """
    #15m
    new_text = ""
    # apply the encoded letters to the text
    for c in text:
        #print "c in text:", c
        if c in coder:
            #print "c in coder:", c
            # alternate method
            #new_text += coder.get(c, None)
            new_text += coder[c]
            #print "new_text:", new_text
            # maintain punctuation
        else:
            new_text += c
            
    return new_text

def apply_shift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. The empty space counts as the 27th letter of the alphabet,
    so spaces should be replaced by a lowercase letter as appropriate.
    Otherwise, lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.
    
    text: string to apply the shift to
    shift: amount to shift the text
    returns: text after being shifted by specified amount.

    Example:
    >>> apply_shift('This is a test.', 8)
    'Apq hq hiham a.'
    """
    #1m
    # shift the text
    return apply_coder(text, build_coder(shift))
   
#
# Problem 2: Codebreaking.
#
def find_best_shift(wordlist, text):
    """
    Decrypts the encoded text and returns the plaintext.

    text: string
    returns: 0 <= int 27

    Example:
    >>> s = apply_coder('Hello, world!', build_encoder(8))
    >>> s
    'Pmttw,hdwztl!'
    >>> find_best_shift(wordlist, s) returns
    8
    >>> apply_coder(s, build_decoder(8)) returns
    'Hello, world!'
    """

    max_real_words = 0
    best_shift = 0

    # search every text shift in the alphabet
    for shift in range(27):
        text1 = apply_coder(text, build_decoder(shift))
        words = text1.split()
        valid_words = 0
        # count English words in each shift
        for word in words:
            if is_word(wordlist, word):
                valid_words += 1
        # pick the shift with the most valid words
        if valid_words > max_real_words:
            max_real_words = valid_words
            best_shift = shift
    return best_shift

##    # check text is string
##    assert isinstance(text, str), "text must be a string"
##    ShiftDict = {}
##    shift = -27
##    textlist = []
##    # each possible shift
##    while shift < 28:
##        # decode text with shift
##        text = apply_coder(text, build_decoder(shift))
##        shift += 1
##        # take words from text by deliminating spaces
##        textlist += text.split()
##        print "textlist:", textlist
##        assert False
##            # check words are in the wordlist
##        for i in range(len(textlist)):
##            if is_word(textlist):
##                # count words that match
##                count_word += 1
##        #add shift + count to dict as key:value
##        ShiftDict[count_words] = shift
##    # find shift with most valid words
##    # sort dict by key then output last key, value

#
# Problem 3: Multi-level encryption.
# 2h
def apply_shifts(text, shifts):
    """
    Applies a sequence of shifts to an input text.

    text: A string to apply the Ceasar shifts to 
    shifts: A list of tuples containing the location each shift should
    begin and the shift offset. Each tuple is of the form (location,
    shift) The shifts are layered: each one is applied from its
    starting position all the way through the end of the string.  
    returns: text after applying the shifts to the appropriate
    positions

    Example:
    >>> apply_shifts("Do Androids Dream of Electric Sheep?", [(0,6), (3, 18), (12, 16)])
    'JufYkaolfapxQdrnzmasmRyrpfdvpmEurrb?'
    # current solution
    'JuFYkaolfapXQdrnzMasMRyrPfdvPMEurrb?'
    # minor bug with capitalization
    # most likely in other function
    """
        
    shifted_text = ""
    lastindex = 0

    # apply each shift to the text at specified index
    for i, (start, shift) in enumerate(shifts):
        shifted_text += text[lastindex:start]
        lastindex = start
        #print "shift text:", shifted_text
        text = apply_coder(text, build_encoder(shift))
        #print "text:", text
        
    shifted_text += text[start: ]
        
    return shifted_text

# split text (first tuple 0 position:second tuple 0 position)
    # encode by shift (first tuple 1 position)
    
    ##    print shifts[0][0]
    ##    print shifts[1][0]
    ##    print shifts[0][1]
    ##    print shifts[2][0]
    ##    print shifts[0][1]
    ##    print shifts[1][1]
    ##    print shifts[2][1]

##    first = 0
##    second = 0
##
##    #iterates through tuples in order
##    for i in xrange(len(shifts)):
##        for j in xrange(len(shifts)):
##            print "j", j
##            # apply coder
##            #apply coder with [0][1]
##            second += 1
##            print "shifts:", shifts[first][second]
##            text = apply_coder(text, build_encoder(shifts[first][second]))
##            print "newtext:", text
##            second -= 1
##            first +=1
##            break
##        
##    return text
    
    #for i in range(len(shifts)):
        #print "i:", i, i, shifts[i-1][i-1]
        #for j in range(i):
            #print "j:", shifts[j][j]
        
    # apply_coder("Hello, world!", build_encoder(3))
 
#
# Problem 4: Multi-level decryption.
# 4h


def find_best_shifts(wordlist, text):
    """
    Given a scrambled string, returns a shift key that will decode the text to
    words in wordlist, or None if there is no such key.

    Hint: Make use of the recursive function
    find_best_shifts_rec(wordlist, text, start)

    wordlist: list of words
    text: scambled text to try to find the words for
    returns: list of tuples.  each tuple is (position in text, amount of shift)
    
    Examples:
    >>> s = random_scrambled(wordlist, 3)
    >>> s
    'eqorqukvqtbmultiform wyy ion'
    >>> shifts = find_best_shifts(wordlist, s)
    >>> shifts
    [(0, 25), (11, 2), (21, 5)]
    >>> apply_shifts(s, shifts)
    'compositor multiform accents'
    >>> s = apply_shifts("Do Androids Dream of Electric Sheep?", [(0,6), (3, 18), (12, 16)])
    >>> s
    'JufYkaolfapxQdrnzmasmRyrpfdvpmEurrb?'
    >>> shifts = find_best_shifts(wordlist, s)
    >>> print apply_shifts(s, shifts)
    Do Androids Dream of Electric Sheep?
    """
    

def find_best_shifts_rec(wordlist, text, start=0):
    """
    Given a scrambled string and a starting position from which
    to decode, returns a shift key that will decode the text to
    words in wordlist, or None if there is no such key.

    Hint: You will find this function much easier to implement
    if you use recursion.

    wordlist: list of words
    text: scambled text to try to find the words for
    start: where to start looking at shifts
    returns: list of tuples.  each tuple is (position in text, amount of shift)
    """
    # this is hard to implement as specified in the pseudo code
    # the pseudo code is missing several important steps such as appending start, shift to a tuple
    
    shifts = []
    
    # for every possible shift 0-27
    for shift in xrange(27):
        print "nshift:", shift
        # set s to be the text before start concatenated with the shifted text after
        s = text[ :start] + apply_coder(text[start: ], build_encoder(shift))
        print "s:", s
        print "s start to end:", s[start: ]
        # look for spaces after location of start
        if " " in s[start: ]:            
            words = text[start: ].split()
            print "word:", words
            # if pre-space contains valid word
            for word in words:
                if is_word(wordlist, word):
                    print "start:", start
                    shifts = [(start, shift)]
##                    try:
##                        shifts.append(tuple((shift, start)))
##                    except:
##                        print "error appending to shifts"
                    start = s.find(" ") +1
                    print "start:", start
                    if start >= len(text):
                        return shifts
                    # recursively run the same algorithm with new start pos
                    return shifts + find_best_shifts_rec(wordlist, text, start)
        # no space found
        else:
            word = s[ :start]
            if is_word(wordlist, word):
                # return a list containing a tuple containing the start parameter and current shift
                shifts = [(start, shift)]
                return shifts
    # no solution in any shifts
    return None       
    
##    words = text.split()
##    print "words:", words
##
##    #skeleton
##    while len(words) > 0:
##        if start == 1:
##            if is_word(wordlist, word):
##                return word in wordlist
##        elif word in wordlist:
##            return find_best_shifts_rec(wordlist, text, start) (words - 1)
##        else:
##            return None


def decrypt_fable():
     """
    Using the methods you created in this problem set,
    decrypt the fable given by the function get_fable_string().
    Once you decrypt the message, be sure to include as a comment
    at the end of this problem set how the fable relates to your
    education at MIT.

    returns: string - fable in plain text
    """
    ### TODO.



    
#What is the moral of the story?
#
#
#
#
#

