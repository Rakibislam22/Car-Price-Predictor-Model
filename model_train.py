import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
import pickle

# ✅ Load dataset
data = pd.read_csv("dataset/car_data.csv")  # change filename if needed
print("✅ Columns found:", list(data.columns))

# ✅ Normalize column names (important!)
data.columns = data.columns.str.lower()

# ✅ Define features and target
X = data[['name', 'year', 'km_driven', 'fuel', 'seller_type', 'transmission', 'owner']]
y = data['selling_price']

# ✅ Encode categorical columns
le = LabelEncoder()
for col in ['name', 'fuel', 'seller_type', 'transmission', 'owner']:
    X[col] = le.fit_transform(X[col])

# ✅ Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ✅ Train model
model = LinearRegression()
model.fit(X_train, y_train)

# ✅ Save model as .pkl
with open("car_price_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved as car_price_model.pkl")
