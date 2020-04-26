import tweepy

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

# Authenticate to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

def push_tweet_to_twitter(tweet):
    # Create API object
    api = tweepy.API(auth, wait_on_rate_limit=True,
                wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
        print("Authentication OK")
    except:
        print("Error during authentication")
    print(tweet)
    api.update_status(tweet)
