import findspark
findspark.init('/home/aamir/spark-2.4.3-bin-hadoop2.7')

import time
import json
from pyspark import SparkContext
from pyspark.streaming import StreamingContext

# filter function:
def filter_tweets(tweet):
    json_tweet = json.loads(tweet)
    if json_tweet.has_key('lang'): # When the lang key was not present it caused issues
        if json_tweet['lang'] == 'en':
            return True # filter() requires a Boolean value
    return False

# SparkContext(“local[1]”) would not work with Streaming bc 2 threads are required
sc = SparkContext("local[2]", "Twitter Demo")
ssc = StreamingContext(sc, 10) #10 is the batch interval in seconds
IP = "localhost"
Port = 5555
lines = ssc.socketTextStream(IP, Port)

# coalesce(1) is used so that final filtered RDD has only one partition i.e one part-00000 file in the directory.
# We use time.time() to make sure there is always a newly created directory, otherwise
# it will throw an Exception.
lines.foreachRDD( lambda rdd: rdd.coalesce(1).saveAsTextFile("/home/aamir/datasets/tweets/%f" % time.time()) )

# You must start the Spark StreamingContext, and await process termination…
ssc.start()
ssc.awaitTermination()
