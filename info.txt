from nltk.sentiment.vader import SentimentIntensityAnalyzer
import sys

def predict_sentiment(args):
    sentence = args.get('sentence')
    sid = SentimentIntensityAnalyzer()
    ss = sid.polarity_scores(sentence)
    sentiment = "Positive"
    if ss['compound'] == 0.00:
      sentiment = 'Neutral'
    elif ss['compound'] < 0.00:
      sentiment = 'Negative'
      
    return sentiment
