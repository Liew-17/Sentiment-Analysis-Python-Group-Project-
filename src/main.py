import pandas as pd
import data_processing as dp
import sentiment_analyzer as sa
import visualizer as v

def run():
    #load and clean data
    df = dp.load_csv('covidvaccine.csv', True, 1000)
    df = dp.parse_dates(df,'date')
    df = dp.clean_text(df,'text')
    df = dp.fill_NA(df,'user_name')
    df = dp.keep_only_columns(df,['user_name','date','text','clean_text'])

    #perform sentiment analysis
    df = sa.analyze_sentiment(df,'clean_text')
    dp.write_new_file(df)

    #visualizations
    v.plot_pie(df,'sentiment_score','sentiment pie chart')
    v.plot_sentiment_trend(df,'date','sentiment_score')

if __name__ == "__main__":
    run()
