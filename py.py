import tensorflow as tf
from transformers import pipeline

sentiment_pipeline = pipeline("sentiment-analysis")
print(sentiment_pipeline("I hate indians!!"))
print("hello")