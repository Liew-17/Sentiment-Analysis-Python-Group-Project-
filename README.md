# Sentiment Analysis Python Group Project


## 1. Overview  
This project performs **sentiment analysis** on Twitter posts containing the hashtag **#CovidVaccine**.  
The main goal is to analyze public opinion toward Covid-19 vaccination by processing tweets, cleaning the text, and applying sentiment classification.  
The project also generates visualizations to highlight sentiment distribution and trends over time.  


## 2. Project Structure  

The repository is organized into three main folders:  

- **`src/`**  
  Contains all Python `.py` modular files. These modules can be imported individually or used together to run the full workflow:  
  - `data_processing.py` – **Data Processing Module**  
    Handles preprocessing tasks: loading CSVs, cleaning text, parsing dates, handling missing values, filtering columns, and saving processed data.  
  - `sentiment_analyzer.py` – **Sentiment Analysis Module**  
    Performs sentiment analysis on text data in a DataFrame using a pre-trained multilingual **BERT** model.  
  - `visualizer.py` – **Data Visualization Module**  
    Provides functions for visualizing data, including **pie charts** (sentiment distribution, scale 1–5) and **line charts** (sentiment trends over time).  
  - `main.py` – **Main Script**  
    Runs the complete workflow:  
      1. Load and preprocess the CSV data.  
      2. Perform sentiment analysis on text and save the processed data to a CSV file.  
      3. Generate visualizations (pie chart and sentiment trend). 

- **`notebook/`**  
  Includes `python_project.ipynb`, a Jupyter Notebook that combines both code and explanatory markdown.  
  - Serves as a step-by-step guide to understand how the `.py` files are generated.  
  - Can be executed directly to reproduce the sentiment analysis and obtain results.  

- **`output/`**  
  Stores generated results, including:  
  - `processed_data.csv`: The cleaned and processed dataset with sentiment labels.  
  - Visualizations:  
    - **Pie chart** showing the distribution of sentiment categories (rated on a scale from 1 to 5, where 1 = very negative and 5 = very positive).
    - **Line chart** illustrating sentiment trends over time.  

## 3. Dataset  
The dataset used for this project was sourced from **Kaggle**.  
It consists of tweets containing the hashtag **#CovidVaccine**.  

To reproduce the analysis, download the dataset from Kaggle:  
https://www.kaggle.com/datasets/kaushiksuresh147/covidvaccine-tweets 
