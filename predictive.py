# 1. Import libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, classification_report, confusion_matrix

# 2. Load dataset
# (Assume you downloaded the CSV from Kaggle and named it 'data.csv')
df = pd.read_csv('data.csv')

# 3. Basic exploration
print(df.shape)
print(df.head())
print(df['diagnosis'].value_counts())

# 4. Pre-processing
# Drop unwanted columns (e.g., ID if present)
if 'id' in df.columns:
    df = df.drop(columns=['id'])
    
# Encode the target (diagnosis: ‘M’ = malignant, ‘B’ = benign)
le = LabelEncoder()
df['diagnosis_enc'] = le.fit_transform(df['diagnosis'])  # M→1, B→0 for example

# Define features & target
X = df.drop(columns=['diagnosis','diagnosis_enc'])
y = df['diagnosis_enc']

# Split into train/test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 5. Train a model
model = LogisticRegression(solver='liblinear', random_state=42)
model.fit(X_train_scaled, y_train)

# 6. Predict & evaluate
y_pred = model.predict(X_test_scaled)

acc = accuracy_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print("Accuracy:", acc)
print("F1 Score:", f1)
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
