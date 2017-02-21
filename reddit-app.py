import praw
import re
import config


def bot_login():
    r = praw.Reddit(username = config.username,
                password = config.password,
                client_id = config.client_id,
                client_secret = config.client_secret,
                user_agent = "Testing a new bot wow v 0.1")
    return r
    
def run_bot(r, subreddit):
    #for comment in r.subreddit('test').comments(limit=500):
    for comment in subreddit.stream.comments():
        if re.search("test", comment.body, re.IGNORECASE) and comment.author.name != 'j-test':            
            print("new comment")
            comment.reply("I also like tests, let's test together!")
            

r = bot_login()
subreddit = r.subreddit("test") # pass in subreddit
run_bot(r, subreddit)