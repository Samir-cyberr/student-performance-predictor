import joblib
import numpy as np

# modelni yuklash
model = joblib.load("model.pkl")

# test input: [study_hours, attendance, sleep_hours]
sample = np.array([[5, 80, 7]])

# prediction
prediction = model.predict(sample)

print(f"Predicted score: {prediction[0]:.2f}")