import praw


# initialize with appropriate values
client_id = ""
client_secret = ""
username = ""
password = ""
user_agent = ""


# creating an authorized reddit instance
reddit = praw.Reddit(client_id=client_id, 
                     client_secret=client_secret,
                     username=username,
                     password= password,
                     user_agent=user_agent)

print(reddit.user.me())

# subreddit where the bot will be live on
target_sub = "espresso"
subreddit = reddit.subreddit(target_sub)

# phrase to trigger the bot
trigger_phrase = "grind finer"

# check every comment in subreddit
for comment in subreddit.stream.comments():
    
    # check if trigger phrase is in comment
    if trigger_phrase in comment.body:

        # comment text
        reply_text = "GRIND FINER!"

        # comment the reply
        comment.reply(reply_text)



