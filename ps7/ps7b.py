#t 1h

import random

def roll_dice(numtrials):

    wins = 0
    #roll_count = 0
    
    # until we get same number
    for i in xrange(numtrials):
        roll_list = []
        #roll_count += 1
        #print roll_count
        print "working:", i
        # roll 5 times, store in list
        for i in xrange(0, 5):
            roll_number = random.randrange(1, 7, 1)
            roll_list.append(roll_number)
        # check if all numbers rolled match
        fivecount = 0
        list_num = roll_list[0]
        for number in roll_list:
            if number == list_num:
                fivecount += 1
        if fivecount == 5:
            wins += 1
        
    return wins
    #print "roll_count:%s" % roll_count

roll_dice(9999)
#roll_dice(100000)
            
##def truefalse():
##
##    true = True
##    false = False
##
##    while true:
##        print true
##        true = False
##
##    while not false:
##        print false
##        false = True

##while True:
##    print random.randrange(1,7,1)
