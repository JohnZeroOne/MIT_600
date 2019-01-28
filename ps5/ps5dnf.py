# 6.00 Problem Set 5
# t 2h
# RSS Feed Filter

import feedparser
import string
import time
from project_util import translate_html
from news_gui import Popup

#-----------------------------------------------------------------------
#
# Problem Set 5

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        summary = translate_html(entry.summary)
        try:
            subject = translate_html(entry.tags[0]['term'])
        except AttributeError:
            subject = ""
        newsStory = NewsStory(guid, title, subject, summary, link)
        ret.append(newsStory)
    return ret

#======================
# Part 1
# Data structure design
#======================

# Problem 1

# data from rss xml
# examples
#<guid isPermaLink="false">tag:news.google.com,2005:cluster=0</guid>
#<title>Top Stories - Google News</title>
#subject - cannot find
#summary - cannot find
#<link>https://news.google.com/news?hl=en&amp;pz=1&amp;ned=us</link>

# new object for news
class NewsStory:
    
    # constructor
    def __init__(self, guid, title, subject, summary, link):
        self.guid = guid
        self.title = title
        self.subject = subject
        self.summary = summary
        self.link = link

    # methods to get parsed data
    def get_guid(self):
        return self.guid
    
    def get_title(self):
        return self.title
    
    def get_subject(self):
        return self.subject
    
    def get_summary(self):
        return self.summary
    
    def get_link(self):
        return self.link

#======================
# Part 2
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        raise NotImplementedError

# Whole Word Triggers
# Problems 2-5
#p2
class WordTrigger(Trigger):
    # constructor
    def __init__(self, word):
        self.word = word
    # methods
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
                return True
        return False

#p3
class TitleTrigger(WordTrigger):
    # constructor
    def __init__(self, title):
        self.title = title
    #
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        return self.is_word_in(story.get_title())
        
#p4    
class SubjectTrigger(WordTrigger):
    # constructor
    def __init__(self, subject):
        self.subject = subject
#p5        
class SummaryTrigger(WordTrigger):
    # constructor
    def __init__(self, summary):
        self.summary = summary

# Composite Triggers
# Problems 6-8
#TODO
class NotTrigger:
    pass
class AndTrigger:
    pass
class OrTrigger:
    pass


# Phrase Trigger
# Question 9

class PhraseTrigger:
    pass


#======================
# Part 3
# Filtering
#======================

def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory-s.
    Returns only those stories for whom
    a trigger in triggerlist fires.
    """
    # TODO: Problem 10
    # This is a placeholder (we're just returning all the stories, with no filtering) 
    # Feel free to change this line!
    return stories

#======================
# Part 4
# User-Specified Triggers
#======================

def readTriggerConfig(filename):
    """
    Returns a list of trigger objects
    that correspond to the rules set
    in the file filename
    """
    # Here's some code that we give you
    # to read in the file and eliminate
    # blank lines and comments
    triggerfile = open(filename, "r")
    all = [ line.rstrip() for line in triggerfile.readlines() ]
    lines = []
    for line in all:
        if len(line) == 0 or line[0] == '#':
            continue
        lines.append(line)

    # TODO: Problem 11
    # 'lines' has a list of lines you need to parse
    # Build a set of triggers from it and
    # return the appropriate ones
    
##import thread
##
##def main_thread(p):
##    # A sample trigger list - you'll replace
##    # this with something more configurable in Problem 11
##    t1 = SubjectTrigger("Obama")
##    t2 = SummaryTrigger("MIT")
##    t3 = PhraseTrigger("Supreme Court")
##    t4 = OrTrigger(t2, t3)
##    triggerlist = [t1, t4]
##    
##    # TODO: Problem 11
##    # After implementing readTriggerConfig, uncomment this line 
##    #triggerlist = readTriggerConfig("triggers.txt")
##
##    guidShown = []
##    
##    while True:
##        print "Polling..."
##
##        # Get stories from Google's Top Stories RSS news feed
##        stories = process("http://news.google.com/?output=rss")
##        # Get stories from Yahoo's Top Stories RSS news feed
##        stories.extend(process("http://rss.news.yahoo.com/rss/topstories"))
##
##        # Only select stories we're interested in
##        stories = filter_stories(stories, triggerlist)
##    
##        # Don't print a story if we have already printed it before
##        newstories = []
##        for story in stories:
##            if story.get_guid() not in guidShown:
##                newstories.append(story)
##        
##        for story in newstories:
##            guidShown.append(story.get_guid())
##            p.newWindow(story)
##
##        print "Sleeping..."
##        time.sleep(SLEEPTIME)
##
##SLEEPTIME = 60 #seconds -- how often we poll
##if __name__ == '__main__':
##    p = Popup()
##    thread.start_new_thread(main_thread, (p,))
##    p.start()
##
##
