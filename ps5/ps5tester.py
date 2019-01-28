import string

def is_word_in(text):
    """
    Returns True if the whole word 'word' is present
    in text, otherwise returns False.
    """
    # translation table for conversion
    table = string.maketrans("","")
    # parse text to remove formatting
    text = text.lower().translate(table, string.punctuation)
    # iterate each word in text and check if word is there
    for words in text:
        if word.lower() in text:
##            print "word:", word
##            print True
            return True
    return False

text = "one, TWO, ThReE"
word = "three"

is_word_in(text)

text = "one, TWO, ThReE"
word = "four"

is_word_in(text)

# works in Python shell but not when script is run??


"""
IDLE 1.2.4      
>>> import string
>>> pring string.punctuation
SyntaxError: invalid syntax
>>> print string.punctuation
!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
>>> word = "this, is a.. test!!"
>>> word.split(string.punctuation)
['this, is a.. test!!']
>>> word.split()
['this,', 'is', 'a..', 'test!!']
>>> word
'this, is a.. test!!'
>>> word.translate(None, string.punctuation)

Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    word.translate(None, string.punctuation)
TypeError: expected a character buffer object
>>> table = string.maketrans("","")
>>> return word.translate(table, string.punctuation)
SyntaxError: 'return' outside function
>>> word.translate(table, string.punctuation)
'this is a test'
>>> word.lower().translate(table, string.punctuation)
'this is a test'
>>> word = 'ThIs, is A.. tEst!!'
>>> word.lower().translate(table, string.punctuation)
'this is a test'
>>> """
