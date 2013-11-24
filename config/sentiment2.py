from imp import reload
import math
import re
import sys

reload(sys)

filenameAFINN = 'EmotionLookupTable.txt'
afinn = dict([(w_s[0], int(w_s[1])) for w_s in [ 
            ws.strip().split('\t') for ws in open(filenameAFINN) ]])

pattern_split = re.compile(r"\W+")

def sentiment(text):
    words = pattern_split.split(text.lower())
    sentiments = [afinn.get(word, 0) for word in words]
    if sentiments:
        sentiment = float(sum(sentiments))/math.sqrt(len(sentiments))
    else:
        sentiment = 0
    return sentiment
