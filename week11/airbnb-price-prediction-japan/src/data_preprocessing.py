import pandas as pd
def load_and_clean(listings_path):
    df = pd.read_csv(listings_path)
    df = df[df['price'].notna()]
    df['price'] = df['price'].replace({'\$':'',',':''}, regex=True).astype(float)
    df = df[df['price'] < df['price'].quantile(0.99)]
    df = df.fillna(df.median(numeric_only=True))
    df = pd.get_dummies(df[['neighbourhood_group','room_type']], drop_first=True)
    return df
