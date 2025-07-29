import pandas as pd
import joblib
from data_preprocessing import load_and_clean

def predict(sample_csv):
    df = load_and_clean(sample_csv)
    model = joblib.load('model.joblib')
    preds = model.predict(df.drop(['price'], axis=1, errors='ignore'))
    df['predicted_price'] = preds
    df.to_csv('predictions.csv', index=False)
    print(df[['price','predicted_price']].head())

if __name__ == '__main__':
    predict('data/listings.csv')
