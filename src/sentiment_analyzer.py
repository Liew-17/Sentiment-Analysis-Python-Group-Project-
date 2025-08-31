from transformers import pipeline
import pandas as pd

sentiment_pipeline = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

def analyze_sentiment(df, target_col):
    try:
        if not isinstance(df, pd.DataFrame):
            raise TypeError("Input must be a pandas DataFrame.")
        if target_col not in df.columns:
            raise ValueError(f"Column '{target_col}' not found in DataFrame.")

        df["sentiment"] = df[target_col].apply(lambda x: sentiment_pipeline(str(x))[0]['label'])
        df["sentiment_score"] = df["sentiment"].str[0].astype(int)

        return df

    except Exception as e:
        print(f"Error in analyze_sentiment: {e}")
        return df
