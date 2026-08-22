from sklearn.tree import DecisionTreeClassifier

# Training examples: number of study hours
hours = [[1], [2], [3], [4], [5], [6]]

# Labels: 0 = not likely to pass, 1 = likely to pass
results = [0, 0, 0, 1, 1, 1]

model = DecisionTreeClassifier(random_state=42)

# Training
model.fit(hours, results)

new_hours = float(input("How many hours did the student study? "))

prediction = model.predict([[new_hours]])[0]

if prediction == 1:
    print("Prediction: likely to pass.")
else:
    print("Prediction: not likely to pass.")

print("Important: this is only a tiny demonstration model.")
print("Real exam results depend on many factors.")
