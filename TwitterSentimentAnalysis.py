import tweepy
from textblob import TextBlob

import plotly.plotly as py
import plotly.graph_objs as go
import plotly
plotly.tools.set_credentials_file(username='<INSERT USER NAME>', api_key='<INSERT API KEY>')

# The accounts to be analyzed.
# @narendramodi177
# @BarackObama
# @realDonaldTrump



# find the most positive tweet and the most negative tweet of a twitter user.
consumer_key='TWITTER CONSUMER KEY'
consumee_secret='TWITTER CONSUMER SECRET'

access_token='TWITTER ACCESS TOKEN'
access_token_secret='TWITTER ACCESS TOKEN SECRET'

auth=tweepy.OAuthHandler(consumer_key, consumee_secret)
auth.set_access_token(access_token, access_token_secret)

api=tweepy.API(auth)
#tweets = []
analysis=[]
sentiment=0
most_positive_tweet=''
xAxis=[]
yAxis=[]
def process_status(status):
#	tweets.append(status)
	analysis.append([status, TextBlob(status.text)])
	
for status in tweepy.Cursor(api.user_timeline,id="@narendramodi177").items():
    # process status here
    process_status(status)


for tweet in analysis:
#	print(tweet[0].text.encode("utf-8"))
#	print(tweet[1].sentiment.polarity)
#	x.append(tweet[0].created_at)
	xAxis.append(tweet[0].id)
	yAxis.append(tweet[1].sentiment.polarity)
	if(tweet[1].sentiment.polarity > sentiment):
		sentiment=tweet[1].sentiment.polarity
		most_positive_tweet=tweet[0].text.encode("utf-8")
	

print("MOST POSITIVE TWEET ")
print(most_positive_tweet)
print("sentiment >>")
print(sentiment)
print(xAxis)
print(yAxis)


trace = go.Scatter(
	x=xAxis,
	y=yAxis,
	name = 'Gaps',
	)

data = [trace]
py.plot(data, filename='basic-line-Modi')


#public_tweets=api.search('Modi')
#for tweets in public_tweets:
#	print(tweets.text)
#	analysis=TextBlob(tweets.text)
#	print(analysis.sentiment)
