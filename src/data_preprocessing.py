import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    return df

def preprocess_data(df):
    X = df[['study_hours', 'attendance', 'sleep_hours']]
    y = df['score']
    return X, y