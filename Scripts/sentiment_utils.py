# sentiment_utils.py

import pandas as pd
from transformers import pipeline

# ---------------------------
# Load Models Once
# ---------------------------

bert_pipeline = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

# ---------------------------
# DistilBERT Sentiment Function
# ---------------------------

def apply_bert_sentiment(df, text_col):
    """
    Adds two columns:
      - 'bert_sentiment' (POSITIVE/NEGATIVE)
      - 'bert_score' (confidence)
      - 'bert_numeric' (+1 or -1)
    """

    df['bert_sentiment'] = df[text_col].apply(lambda x: bert_pipeline(x)[0]['label'])
    df['bert_score'] = df[text_col].apply(lambda x: bert_pipeline(x)[0]['score'])
    df['bert_numeric'] = df['bert_sentiment'].map({'POSITIVE': 1, 'NEGATIVE': -1})
    return df



# ---------------------------
# Aggregation Function
# ---------------------------
def aggregate_sentiment(df, bank_col, rating_col, sentiment_col):
    """
    Returns mean sentiment grouped by bank and rating.
    """

    return (
        df.groupby([bank_col, rating_col])[sentiment_col]
        .mean()
        .reset_index()
    )
 