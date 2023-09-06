import praw
import os
import time
from ArticlesFound import Articles

"""
Praw scans r/boulder once every 5~ minutes for a post containing a dailycamera link
If found, send link to Articles.py
Interface with articles.py to format a new post, and comment it on the found post.
"""

reddit = praw.Reddit("DCBot") #Logging into reddit via PRAW and creating active instance.
boulder = reddit.subreddit("Boulder") #Creating an isntance directly relating to the subreddit in question.
test = reddit.subreddit("test") #Creating an instance for the test subreddit (for testing)
test2 = reddit.subreddit("funny")
post_link = "" #Holds the link embedded in a post. Is reset for every new post.
daily_camera_detector = -2 #Holds a number that is set if program finds it to be a daily camera link. Is reset for every new post.


for submission in test.stream.submissions(skip_existing = True): #Opens a stream that checks every new post in selected subreddit.
    
    if not submission.is_self: #Only processes posts that contain a link outside of reddit (eg to a news website like daily camera)
    #Validates if the link-post is a link to the daily camera.
        post_link = submission.url #Saves the link contained in the post.
        daily_camera_detector = post_link.find('dailycamera.com') #Determines if the link is a daily camera link.
        
        if not daily_camera_detector == -1: #Only executes if it is a daily camera link.
        #Parse data from the article at post it in the comments of the matching post.
            current_article = Articles(post_link)
            #TODO - format a post for reddit and submit it to the comments with article info.
