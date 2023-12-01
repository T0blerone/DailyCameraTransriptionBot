import praw
import os
import time
import schedule
from ArticlesFound import Articles

reddit = praw.Reddit("DCBot") #Logging into reddit via PRAW and creating active instance.
boulder = reddit.subreddit("Boulder") #Creating an isntance directly relating to the subreddit in question.
test = reddit.subreddit("test") #Creating an instance for the test subreddit (for testing)
post_link = "" #Holds the link embedded in a post. Is reset for every new post.
daily_camera_detector = -2 #Holds a number that is set if program finds it to be a daily camera link. Is reset for every new post.
content_to_be_posted = "" #A temp variable to assemble a string to be posted.
log = open("log.txt", "a") #Opening a file stream that logs all submissions made by the bot.

def createPost(article): #Function that assembles the text to be commented by the bot.
    content_to_be_posted = "#[" #Formatting
    content_to_be_posted += current_article.getTitle() #Title
    content_to_be_posted += "](" #Formatting
    content_to_be_posted += post_link #Creating Hyperlink
    content_to_be_posted += ")\n\n" #Formatting
    content_to_be_posted += current_article.getText() #Article Text
    content_to_be_posted += "\n\n\n\n ^Beep ^Boop ^I'm ^a ^bot. ^Hope ^this ^helped!" #Disclaimer
    return content_to_be_posted

for submission in test.stream.submissions(skip_existing = True): #Opens a stream that checks every new post in selected subreddit.
    if not submission.is_self: #Only processes posts that contain a link outside of reddit (eg to a news website like daily camera)
    #Validates if the link-post is a link to the daily camera.
        post_link = submission.url #Saves the link contained in the post.
        daily_camera_detector = post_link.find('dailycamera.com/20') #Determines if the link is a daily camera article link.
        
        if not daily_camera_detector == -1: #Only executes if it is a daily camera link.
        #Parse data from the article at post it in the comments of the matching post.
            current_article = Articles(post_link) #Creating article object to parse data from.
            log.write("\nTitle: " + str(submission.title) + " | Post ID: " + str(submission.id) + " | Time Posted: " + str(submission.created_utc)) #Writing to the log submission info
            log.flush() #Updating the log in real time
            submission.reply(createPost(content_to_be_posted)) #Posting comment.