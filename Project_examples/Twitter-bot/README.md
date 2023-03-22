# Twitter bot:

# Requirements:

* pip install the following:
    * tweepy (A library that connects and draws data from twitter)
    * re (A library which handles regular expressions)

* Twitter Developer Account credentials. Once you have an acconut you can access the following:
    * consumer_key
    * consumer_secret
    * access_token
    * access_token_secret
    * These then need to be inputed into lines 15-18, replacing the "XXXXXXXXXXXXXXXXXXXXXXXXXXXX" placeholders.

* Topic you want to search for. On line 93 (`tweets = api.get_tweets(query = 'TFL Strikes', count = 200)`), you can input a string you want to access and the number of most recent tweets to collec.t

# Running the program

Once the requirements have been furfulled, the program can be run by navigating to the folder `main.py` is saved in, using the command line prompt. Then executing `python ./main.py`

