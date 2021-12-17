#!/usr/bin/env python

import json
from pulsar import Function
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

class Chat(Function):
    def __init__(self):
        pass

    def process(self, input, context):
        logger = context.get_logger()
        logger.info("Message Content: {0}".format(input))
        fields = json.loads(input)
        sid = SentimentIntensityAnalyzer()
        ss = sid.polarity_scores(fields['comment'])
        logger.info("Polarity: {0}".format(ss['compound']))
        sentimentVal = 'Neutral'
        if ss['compound'] == 0.00:
            sentimentVal = 'Neutral'
        elif ss['compound'] < 0.00:
            sentimentVal = 'Negative'
        else:
            sentimentVal = 'Positive'
        return sentimentVal
