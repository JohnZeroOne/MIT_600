# working

import re
ans_word = "detonator"
guess = "a"
temp = re.sub(guess, '!', ans_word)
print temp
temp2 = re.sub('[^!]', '_', temp)
print temp2
progress = re.sub('!', guess, temp2)
print progress


    

##def letter_helper():
##
##    progressStr = ""
##    ans_word = "detonator"
##    guess = "a"
##    progressLst = []
##    
##    for i in range(len(ans_word)):
##        progressLst.insert(0, ".")
##
##    ans_word_temp = ans_word.replace("a", "!")
##    ans_word = ans_word.replace(ans_word, "_")
##    print "temp", ans_word_temp
##    print "ans", ans_word

##def letter_helper():
##
##    ans_word = "detonator"
##    guess = "a"
##
##    print re.sub("a", "!", 1)
##
##letter_helper()

##def letter_helper_old():
##    ans_word = "abbaccus a"
##    guess = "a"
##    # find index position/s of guess inside ans_word
##    indices = [index for index, value in enumerate(ans_word) if value == guess]
##    print(indices)
##    # create new progress word with those indexes and the letter appended
##    
##    # progress()
##
            
##def letter_helper():
##
##    progressStr = ""
##    ans_word = "detonator"
##    guess = "a"
##    progressLst = []
##    
##    for i in range(len(ans_word)):
##        progressLst.insert(0, ".")
##
##    ans_word_temp = ans_word.replace("a", "!")
##    ans_word = ans_word.replace(answer_word, "_")
##    print "temp", ans_word_temp
##    print "ans", ans_word

## letter_helper()
