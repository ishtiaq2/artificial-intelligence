"""
02 – How a computer adjusts its "weights" (the learning process)

In a real neural network the computer has many numbers called weights.
Training = slowly changing those numbers so the predictions get better.

Here we have only ONE number to learn: the weight of "hours slept".
We start with a bad guess and improve it using the error.
"""

# Training examples: hours → tired (1) or not (0)
examples = [
    (3, 1),
    (4, 1),
    (5, 1),
    (6, 0),
    (7, 0),
    (8, 0),
]

# Start with a random/wrong guess
weight = 0.1          # how strongly "hours" affects the prediction
bias   = 0.5
learning_rate = 0.05

print("Starting weight:", weight)
print("We will show the examples many times and nudge the weight...\n")

for epoch in range(1, 21):
    total_error = 0
    for hours, true_label in examples:
        # Forward: make a prediction (very simple linear model)
        prediction = hours * weight + bias
        # Turn into 0 or 1 style decision (just for display)
        predicted_label = 1 if prediction < 0.5 else 0

        # Error = how wrong we were
        error = true_label - prediction
        total_error += abs(error)

        # Backprop-style update: change weight in the direction that reduces error
        weight = weight + learning_rate * error * hours
        bias   = bias   + learning_rate * error

    if epoch % 5 == 0:
        print(f"Round {epoch:2d}  |  weight = {weight:.3f}  |  average error ≈ {total_error/len(examples):.3f}")

print("\nFinal learned weight:", round(weight, 3))
print("Interpretation: the computer discovered that more hours → less tiredness")
print("(negative relationship between hours and the 'tired' score)")
