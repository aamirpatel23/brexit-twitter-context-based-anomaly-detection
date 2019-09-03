# brexit-twitter-context-based-anomaly-detection

### Project based on [COMP702 MSC PROJECT](https://cgi.csc.liv.ac.uk/~comp702/) module at University of Liverpool

The main purpose of this project is to investigate and to understand the context of large-scale of tweets by using machine learning to detect group’s (collective) #brexit topics contexts.

The model can be divided into four stages:
- Twitter Streaming
- Tweets Preprocessing
- Topic Modeling
- Anomaly Detection

#### 1. Twitter Streaming

Two methods have been implemented to stream tweets. It has been observed **Spark + Tweepy** method when executed in local mode on one machine is significantly slower than **Tweepy** method in the same environment.
- **Tweepy** - [TwitterStreaming_Tweepy.py](https://github.com/aamirpatel23/brexit-twitter-context-based-anomaly-detection/blob/master/TwitterStreaming_Tweepy.py) streams tweets using twitter streaming api and tweepy and saves the "text" of the tweets in csv format. **Note:** The code might return error 420 after running for 1 min, reason being rate limit imposed by twitter. Wait for atleast 10-15 min and then re-run the code to start streaming tweets. The tweets will continue to append to the previously saved tweets in the csv file.

- **Spark + Tweepy** - [TwitterStreaming_SparkTweepy.py](https://github.com/aamirpatel23/brexit-twitter-context-based-anomaly-detection/blob/master/TwitterStreaming_SparkTweepy.py) waits on localhost:5555 until the next script
[TwitterStreaming_Spark.py](https://github.com/aamirpatel23/brexit-twitter-context-based-anomaly-detection/blob/master/TwitterStreaming_Spark.py) runs. The tweets are stored in partition files (JSON format) which can then be merged into one file using merge file commands.

#### 2. Tweets Preprocessing

A series of preprocessing operations such as removing return handles, twitter handles, URLs, special characters, numbers, punctuations and stopwords are performed on the twitter dataset to remove redundant and unimportant data. 

#### 3. Topic Modeling

To detect the context (topics) of tweets for #brexit, unsupervised machine learning algorithms, Latent Dirichlet Allocation (LDA) and Non-Negative Matrix Factorization (NMF) are implemented. 
There are two implementations of LDA: **Gensim LDA** and **Mallet LDA**. Mallet LDA gives better quality of topics and high coherence score when evaluating the model.
The analysis of the topics extends to finding optimal number of topics for a given dataset, finding dominant topics, finding the most representative tweet for each topic, and topic distribution across the collection of tweets.

#### 4. Anomaly Detection

The results obtained from topic modelling stage are the list of contexts (topics) related to #brexit. To detect anomalies, we find the topics that contain words related to profanity, racism, terrorism, and war. These topics can then be used to identify the corrosponding tweets expressing unusual behavior.

***
## Installing Packages

The project has been carried using [Python 3.6.8](https://www.python.org/downloads/), [Spark-2.4.3-bin-hadoop2.7](https://spark.apache.org/downloads.html), [Java 12.0.1](https://www.oracle.com/technetwork/java/javase/downloads/index.html), [Mallet 2.0.8](http://mallet.cs.umass.edu/) and the python packages present in [requirements.txt](https://github.com/aamirpatel23/brexit-twitter-context-based-anomaly-detection/blob/master/requirements.txt) that can be installed individually using ```pip3 install``` command or by executing the requirements.txt using ```pip3 install -r requirements.txt```

***
## Order of Execution of Codes

#### 1. Twitter Streaming

- If you want to use **only tweepy** to stream the tweets, then open a terminal and enter ```python3 TwitterStreaming_Tweepy.py```

- If you want to make use of **Spark and Tweepy** for streaming tweets, then open a terminal and enter ```python3 TwitterStreaming_SparkTweepy.py``` and then open another terminal and enter ```python3 TwitterStreaming_Spark.py``` 

    - When you execute these files, the tweets will start streaming and sub-folders would be created in the **tweets** folder at the path mentioned. Use ```find /home/aamir/datasets/tweets -type f -name 'part-00000' -exec cat {} + >mergedTweets.json``` to merge the partition files into one json file.
    
    - To convert json file to csv, use [JSON_to_CSV.ipynb](https://github.com/aamirpatel23/brexit-twitter-context-based-anomaly-detection/blob/master/JSON_to_CSV.ipynb) notebook.

#### BONUS:  To skip the above Twitter Streaming step, extract the dataset from [brexit.zip](https://github.com/aamirpatel23/brexit-twitter-context-based-anomaly-detection/blob/master/brexit.zip), continue to next step and update the paths where needed.

#### 2. Preprocessing, Topic Modeling, and Anomaly Detection

- Use Jupyter notebook to execute [LDA.ipynb](https://github.com/aamirpatel23/brexit-twitter-context-based-anomaly-detection/blob/master/LDA.ipynb) and [NMF.ipynb](https://github.com/aamirpatel23/brexit-twitter-context-based-anomaly-detection/blob/master/NMF.ipynb). Both notebooks perform preprocessing and topic modeling, however, [LDA.ipynb](https://github.com/aamirpatel23/brexit-twitter-context-based-anomaly-detection/blob/master/LDA.ipynb) contains experiments to detect anomalies.
