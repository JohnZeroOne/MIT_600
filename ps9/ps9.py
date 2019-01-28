# 6.00 Problem Set 9
#
# Intelligent Course Advisor
#
# Name:
# Collaborators:
# Time: 120m
#

SUBJECT_FILENAME = "subjects.txt"
SHORT_SUBJECT_FILENAME = "shortened_subjects.txt"
VALUE, WORK = 0, 1

#
# Problem 1: Building A Subject Dictionary
#
def loadSubjects(filename):
    """
    Returns a dictionary mapping subject name to (value, work), where the name
    is a string and the value and work are integers. The subject information is
    read from the file named by the string filename. Each line of the file
    contains a string of the form "name,value,work".

    returns: dictionary mapping subject name to (value, work)
    """

    #loadSubjects("shortened_subjects.txt")
    
    # The following sample code reads lines from the specified file and prints
    # each one.

    inputFile = open(filename)
    subject_dict = {}
    parse_list = []
    # read the file, remove formatting, split 3nth elements into lists of vals
    for line in inputFile:
        #print line
        line = line.strip()
        parse_list.append(line.split(','))
    # build a dictionary from lists with course: value, work as key:val pairs
    for tlist in parse_list:
        #print tlist
        subject_dict[tlist[0]] = int(tlist[1]), int(tlist[2])

    return subject_dict

def printSubjects(subjects):
    """
    Prints a string containing name, value, and work of each subject in
    the dictionary of subjects and total value and work of all subjects
    """
    totalVal, totalWork = 0,0
    if len(subjects) == 0:
        return 'Empty SubjectList'
    res = 'Course\tValue\tWork\n======\t====\t=====\n'
    subNames = subjects.keys()
    subNames.sort()
    for s in subNames:
        val = subjects[s][VALUE]
        work = subjects[s][WORK]
        res = res + s + '\t' + str(val) + '\t' + str(work) + '\n'
        totalVal += val
        totalWork += work
    res = res + '\nTotal Value:\t' + str(totalVal) +'\n'
    res = res + 'Total Work:\t' + str(totalWork) + '\n'
    print res

#
# Problem 2: Subject Selection By Greedy Optimization
#

def cmpValue(subInfo1, subInfo2):
    """
    Returns True if value in (value, work) tuple subInfo1 is GREATER than
    value in (value, work) tuple in subInfo2
    """
    return subInfo1[0] > subInfo2[0]

def cmpWork(subInfo1, subInfo2):
    """
    Returns True if work in (value, work) tuple subInfo1 is LESS than than work
    in (value, work) tuple in subInfo2
    """
    return subInfo1[1] < subInfo2[1]

def cmpRatio(subInfo1, subInfo2):
    """
    Returns True if value/work in (value, work) tuple subInfo1 is 
    GREATER than value/work in (value, work) tuple in subInfo2
    """
##    one = subInfo1[0]/subInfo1[1]
##    two = subInfo2[0]/subInfo2[1]
    #subInfo1[0]/subInfo1[1] > subInfo2[0]/subInfo2[1]
    
    return subInfo1 > subInfo2

def greedyAdvisor(subjects, maxWork, comparator):
    """
    Returns a dictionary mapping subject name to (value, work) which includes
    subjects selected by the algorithm, such that the total work of subjects in
    the dictionary is not greater than maxWork.  The subjects are chosen using
    a greedy algorithm.  The subjects dictionary should not be mutated.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    comparator: function taking two tuples and returning a bool
    returns: dictionary mapping subject name to (value, work)
    """

##    print subjects
##
##    for course in subjects:
##        print course
##        if comparator(course, course):
##            return "yes"
##        else:
##            return "no"

    #subjects = loadSubjects("shortened_subjects.txt")
    #greedyAdvisor(subjects, 20, cmpRatio)
    try:
        assert maxWork >= 0
        assert isinstance(maxWork, int)
    except:
        raise Exception
    
    greedy_dict = {}
    current_work = 0
    i = 0
    #how to check previous course against current in iteration?

    # until work req. is met
    while current_work < maxWork and i < len(subjects):
        # go through dict
        for course, data in subjects.iteritems():
            subInfo1 = data
            subInfo2 = data # previous iteration
            #print course, data
            # implement greedy choice
            if comparator(subInfo1, subInfo2):
                greedy_dict[course] = data
            # calc current work
            current_work = subInfo1[1] + subInfo2[1]
            print "current_work, max_work %s" % (current_work, max_work)
        i += 1

    raise NotImplementedError
    return greedy_dict
            
        

#
# Problem 3: Subject Selection By Brute Force
#
def bruteForceAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work), which
    represents the globally optimal selection of subjects using a brute force
    algorithm.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    # TODO...
    raise NotImplementedError

