# A.Connect to Twitter, Print out our input
from textblob import TextBlob
import sys, tweepy
import matplotlib.pyplot as plt

# Twitter Keys - Go to Twitter
consumerKey = "x"
consumerSecret = "x"
accessToken = "x"
accessTokenSecret = "x"


# Establish a connection to Twitter
auth = tweepy.OAuthHandler(consumer_key=consumerKey, consumer_secret=consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

# Get search term and number of tweets
searchTerm = input("Enter twitter handle/hashtag to search about: ")
noOfSearchTerms = int(input("Enter how many tweets to analyze: "))

# This will show us our what input we're getting
print("How people are reacting on " + searchTerm + " by analyzing " + str(noOfSearchTerms) + " Tweets.")

