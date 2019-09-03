import pandas as pd
import numpy as np
import tweepy
import csv

import warnings
warnings.filterwarnings("ignore")

####input your credentials here (do not ignore the quotes)
consumer_key = 'YOUR CONSUMER KEY'
consumer_secret = 'YOUR CONSUMER SECRET'
access_token = 'YOUR ACCESS TOKEN'
access_token_secret = 'YOUR ACCESS TOKEN SECRET'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit = False)

# Open/Create a file to append data
csvFile = open('/home/aamir/datasets/brexit_tweepy.csv', 'a')

#Use csv Writer
csvWriter = csv.writer(csvFile)

# update/change the search keyword or language as per your inputs
for tweet in tweepy.Cursor(api.search, q = "#brexit", lang = "en").items():
    # to print the tweets in terminal (cmd), uncomment the line below
    #print (tweet.text)
    csvWriter.writerow([tweet.text.encode('utf-8')])
