import tweepy
from textblob import TextBlob

consumer_key = 'Y65IPyLUJ24S0ha6BkvNOIVva'
consumer_secret = 'XtOuNcRQPjwVGBNN7aiF3yvpRu5hfNfn0AyZl6WG5tvVgPTEGM'

access_token = '783367485995249664-pBGCOtJqMI10QcjFENrw1WF7xbiu4EM'
access_token_secret = 'ORPty7W48J3KrFJNVZatDGhKm2XG5QqkeDID4OUxLjo37'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)

