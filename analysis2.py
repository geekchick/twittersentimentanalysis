# Print out Tweets to console
from textblob import TextBlob
import sys, tweepy
import matplotlib.pyplot as plt

# Twitter Keys - Go to Twitter and
consumerKey = "x"
consumerSecret = "x"
accessToken = "x"
accessTokenSecret = "x"


# Establish a connection to Twitter
auth = tweepy.OAuthHandler(consumer_key=consumerKey, consumer_secret=consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

# Get search term and number of tweets
searchTerm = input("Enter keyword/hashtag to search about: ")
noOfSearchTerms = int(input("Enter how many tweets to analyze: "))


# Get the number of tweets related to search term
tweets = tweepy.Cursor(api.search, q=searchTerm).items(noOfSearchTerms)

# Loop through each tweet and print to console
for tweet in tweets:
    print(tweet.text)