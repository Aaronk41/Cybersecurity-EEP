import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib
from data_preprocessing import load_and_clean

def train(listings_path):
    df = load_and_clean(listings_path)
    X = df.drop(['price','id','name','host_id'], axis=1, errors='ignore')
    y = df['price']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print("RMSE:", mean_squared_error(y_test, y_pred, squared=False))
    print("R2:", r2_score(y_test, y_pred))
    joblib.dump(model, 'model.joblib')

if __name__ == '__main__':
    train('data/listings.csv')
