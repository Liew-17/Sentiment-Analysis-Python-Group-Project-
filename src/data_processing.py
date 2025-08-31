
import pandas as pd
import re

def load_csv(file_path, do_sample=False, sample_size=3000):
    try:
        df = pd.read_csv(file_path, low_memory=False, on_bad_lines="skip")
        print(f"Loaded {file_path} successfully.")

        if do_sample:
          if len(df) > sample_size:
            df = df.sample(n=sample_size, random_state=42)

        return df

    except Exception as e:
        print(f"Error loading {file_path}: {e}")
        return None

def parse_dates(df, date_col):
    try:
        if date_col not in df.columns:
            raise ValueError(f"Column '{date_col}' not found in DataFrame.")
        if not isinstance(df, pd.DataFrame):
            raise TypeError("Input must be a pandas DataFrame.")

        s = df[date_col].astype(str).str.strip().str.replace(r'\s+', ' ', regex=True)

        formats = [
            '%d/%m/%Y %I:%M:%S %p',
            '%d-%m-%Y %H:%M',
            '%Y-%m-%d %H:%M:%S',
            '%d/%m/%Y',
            '%Y-%m-%d'
        ]

        parsed = pd.Series([pd.NaT]*len(s), index=s.index) #create a empty list with index corresponding to df

        for fmt in formats:
            mask = parsed.isna() #find emptry space
            try:
                parsed[mask] = pd.to_datetime(s[mask], format=fmt, errors='coerce') #try convert date object
            except:
                continue

        df[date_col] = parsed

    except Exception as e:
        print(f"Error parse_dates: {e}")

    return df[df[date_col].notna()]

def clean_text(df, text_col):
    try:
        if text_col not in df.columns:
            raise ValueError(f"Column '{text_col}' not found in DataFrame.")
        if not isinstance(df, pd.DataFrame):
            raise TypeError("Input must be a pandas DataFrame.")

        def _clean_single_text(text):
            if not isinstance(text, str):
                return ""
            text = re.sub(r"[^a-zA-Z0-9\s]", " ", text)
            text = text.lower()
            return " ".join(text.split()) 

        df['clean_text'] = df[text_col].apply(_clean_single_text)
        return df

    except Exception as e:
        print(f"Error in clean_text: {e}")
        return df

def fill_NA(df, target_col):
    try:
        if target_col not in df.columns:
            raise ValueError(f"Column '{target_col}' not found in DataFrame.")
        if not isinstance(df, pd.DataFrame):
            raise TypeError("Input must be a pandas DataFrame.")

        df[target_col] = df[target_col].fillna("unknown")
        return df

    except Exception as e:
        print(f"Error in fill_NA: {e}")
        return df

def keep_only_columns(df, columns_to_keep):
    try:
        if not isinstance(df, pd.DataFrame):
            raise TypeError("Input must be a pandas DataFrame.")
        if not isinstance(columns_to_keep, list):
            raise TypeError("columns_to_keep must be a list.")

        #keep only columns that exist in the DataFrame
        existing_cols = [col for col in columns_to_keep if col in df.columns]
        return df[existing_cols]

    except Exception as e:
        print(f"Error: {e}")
        return df

def write_new_file(df, filename="processed_data.csv"):
      try:
        df.to_csv(filename, index=False, encoding="utf-8")
        print(f"File successfully saved as {filename}")
      except Exception as e:
        print(f"Error saving file: {e}")
