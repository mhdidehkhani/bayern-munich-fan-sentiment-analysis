import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

text = "Bayern Munich played a fantastic match today!"

score = analyzer.polarity_scores(text)

print(score)
