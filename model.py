import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import pickle

# Load dataset
data = pd.read_csv("data.csv")

# Inputs (X) and Output (y)
X = data[["sleep_hours", "study_hours", "stress_level", "mood_score"]]
y = data["risk"]

# Train model
model = DecisionTreeClassifier()
model.fit(X, y)

# Save trained model
pickle.dump(model, open("model.pkl", "wb"))

print("Model trained successfully")
