import findspark
# enter the path of your spark directory
findspark.init('/home/aamir/spark-2.4.3-bin-hadoop2.7')

import os
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import socket
import json

# enter twitter credentials (do not ignore the quotes)
consumer_key    = 'YOUR CONSUMER KEY'
consumer_secret = 'YOUR CONSUMER SECRET'
access_token    = 'YOUR ACCESS TOKEN'
access_secret   = 'YOUR ACCESS SECRET'

class TweetsListener(StreamListener):

	def __init__(self, csocket):
        	self.client_socket = csocket

	def on_data(self, data):
		try:
			print(data.split('\n'))
			self.client_socket.send(bytes(data, 'utf-8'))
			return True
		except BaseException as e:
			print("Error on_data: %s" % str(e))
		return True

	def on_error(self, status):
		#print(status)
		return True

def sendData(c_socket):
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_secret)

	twitter_stream = Stream(auth, TweetsListener(c_socket))
	
	# modify the language and keyword tracking inputs as per your choice
	twitter_stream.filter(languages=['en'], track=['#brexit'])

if __name__ == "__main__":
	s = socket.socket()     # Create a socket object
	host = "localhost"      # Get local machine name
	port = 5555             # Reserve a port for your service.
	s.bind((host, port))    # Bind to the port

	print("Listening on port: %s" % str(port))

	s.listen(5)                 # Now wait for client connection.
	c, addr = s.accept()        # Establish connection with client.

	print( "Received request from: " + str( addr ) )

	sendData( c )
