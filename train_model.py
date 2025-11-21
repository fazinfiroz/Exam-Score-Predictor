import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
import dill

# Load dataset
df = pd.read_csv('student_scores.csv')
X = df[['study_hours', 'attendance']]
y = df['score']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate accuracy
y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)
print(f"✅ Model Accuracy (R² Score): {r2:.2f}")

# Save model
with open('model.dill', 'wb') as f:
    dill.dump(model, f)

print("✅ Model trained and saved to model.dill")
