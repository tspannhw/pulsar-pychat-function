#!/usr/bin/env python

from pulsar import Function
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import json

class Chat(Function):
    def __init__(self):
        pass

    def process(self, input, context):
        logger = context.get_logger()
        logger.info("Message Content: {0}".format(input))
        msg_id = context.get_message_id()

        fields = json.loads(input)
        sid = SentimentIntensityAnalyzer()
        ss = sid.polarity_scores(fields["comment"])
        logger.info("Polarity: {0}".format(ss['compound']))
        sentimentVal = 'Neutral'
        if ss['compound'] == 0.00:
            sentimentVal = 'Neutral'
        elif ss['compound'] < 0.00:
            sentimentVal = 'Negative'
        else:
            sentimentVal = 'Positive'
        row = { }

        row['id'] = str(msg_id)
        row['sentiment'] = str(sentimentVal)
        row['userInfo'] = str(fields["userInfo"])
        row['comment'] = str(fields["comment"])
        row['contactInfo'] = str(fields["contactInfo"])
        json_string = json.dumps(row)
        return json_string
