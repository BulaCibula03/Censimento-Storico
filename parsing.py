import pandas as pd

def parse():
    df = pd.read_csv('file.csv')
    print(df)
    return df
