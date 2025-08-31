import matplotlib.pyplot as plt
import pandas as pd

def plot_pie(df, value_col, title):
    try:
        if not isinstance(df, pd.DataFrame):
            raise TypeError("Input must be a pandas DataFrame.")
        if value_col not in df.columns:
            raise ValueError(f"Column '{value_col}' not found in DataFrame.")

        counts = df[value_col].value_counts()
        counts.plot(kind="pie", autopct='%1.1f%%', startangle=90, figsize=(15,15))
        plt.title(title)
        plt.ylabel("")
        plt.show()

    except Exception as e:
        print(f"Error generating pie chart: {e}")

def plot_sentiment_trend(df, date_col, sentiment_col):
    try:
        if not isinstance(df, pd.DataFrame):
            raise TypeError("Input must be a pandas DataFrame.")
        if date_col not in df.columns:
            raise ValueError(f"Column '{date_col}' not found in DataFrame.")
        if sentiment_col not in df.columns:
            raise ValueError(f"Column '{sentiment_col}' not found in DataFrame.")

        df_copy = df.copy()

        #grp by year month
        df_copy['year_month'] = df_copy[date_col].dt.to_period('M')
        monthly = df_copy.groupby('year_month').agg({sentiment_col: ['mean', 'count']})
        monthly.columns = ['avg_sentiment', 'count']

        monthly = monthly.reset_index()
        monthly['year_month'] = monthly['year_month'].astype(str)
        monthly = monthly.sort_values('year_month')

        #plot average sentiment
        plt.figure(figsize=(14, 6))
        plt.plot(monthly['year_month'], monthly['avg_sentiment'], marker='o', linestyle='-')
        plt.title(f"Monthly Average Sentiment ({sentiment_col})")
        plt.xlabel("Month")
        plt.ylabel(f"Average {sentiment_col}")

        #add number of post to each month
        for i, row in monthly.iterrows():
            plt.text(i, row['avg_sentiment'] + 0.05, str(row['count']), ha='center', va='bottom', fontsize=8)

        plt.text(len(monthly)-1, monthly['avg_sentiment'].max() + 0.25, "Number above each point = number of posts in that month", fontsize=9, ha='right')

        plt.xticks(rotation=45)
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"Error generating sentiment trend: {e}")
