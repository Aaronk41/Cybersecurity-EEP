# python/train_model.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import joblib
import os

# Load dataset
df = pd.read_csv('data/pokemon.csv')

# Select features and target
features = ['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed', 'Total']
df = df.dropna(subset=features + ['Type 1'])
X = df[features]
y = df['Type 1']

# Encode target labels
le = LabelEncoder()
y_encoded = le.fit_transform(y)

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, stratify=y_encoded, random_state=42)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train Random Forest model
clf = RandomForestClassifier(n_estimators=200, max_depth=10, random_state=42)
clf.fit(X_train_scaled, y_train)

# Evaluate model
y_pred = clf.predict(X_test_scaled)
print("Classification Report:")
print(classification_report(y_test, y_pred, target_names=le.classes_))

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Save model
os.makedirs("model", exist_ok=True)
joblib.dump({'model': clf, 'scaler': scaler, 'le': le}, 'model/pokemon_type_predictor.pkl')
print("Model saved to model/pokemon_type_predictor.pkl")
